import random
import psycopg2
from flask import Flask, request, jsonify, abort

db_name = "postgres"
db_user = "postgres"
db_password = "postgres"

db_host = "host.docker.internal"

ports = ['5432', '5433', '5434']

db_shards = []
for i in ports:
    db_shards.append(
        psycopg2.connect(
            host=db_host,
            port=i,
            database=db_name,
            user=db_user,
            password=db_password
        )
    )

app = Flask(__name__)

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(num, alphabet):
    """Encode a positive number into Base X and return the string.

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    arr_append = arr.append  # Extract bound-method for faster access.
    _divmod = divmod  # Access to locals is faster.
    base = len(alphabet)
    while num:
        num, rem = _divmod(num, base)
        arr_append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def decode(string, alphabet=BASE62):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for decoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

@app.route("/<id>")
def get(id):
    if id.startswith('favicon'):
        abort(404)
    num = decode(id)
    shard_num = num & ((1 << 5) - 1)
    url_id = num >> 5
    curr = db_shards[shard_num].cursor()
    curr.execute("SELECT id, url from URLS where id = %s limit 1", (url_id,))
    data = curr.fetchone()
    return f"{data[1]}"

@app.route('/create', methods=['POST'])
def create_short_url():
    data = request.json
    url = data['url']
    shard_num = random.randint(1, len(ports)) - 1

    conn = db_shards[shard_num]
    curr = conn.cursor()
    curr.execute("INSERT INTO URLS (url) VALUES (%s) RETURNING id", (url,))
    conn.commit()
    data = curr.fetchone()
    url_id = data[0]

    short = (url_id << 5) | shard_num
    return jsonify({
        'url': url,
        'short': encode(short, alphabet=BASE62),
        'shard': shard_num
    })

app.run(port=8000)
