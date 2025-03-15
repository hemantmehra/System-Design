# URL Shortener
Uses multiple postgres shards to store id and url.

url is shortened by converting url_id to base62 number.
url_id is generated using (table_id | (shard_id << 5))
shard_id is picked at random by flask server.

## Steps to build 
1. Build docker image
```
docker build . -t pgshard
```

2. Create shard containers
```
docker run --name pgshard1 -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d pgshard
docker run --name pgshard2 -p 5433:5432 -e POSTGRES_PASSWORD=postgres -d pgshard
docker run --name pgshard3 -p 5434:5432 -e POSTGRES_PASSWORD=postgres -d pgshard
```

3. Run flask server
```
python server.py
```
