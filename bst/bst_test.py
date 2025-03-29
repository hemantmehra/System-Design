import random
from bst import bst_create, bst_inorder, bst_search, bst_height
from bst import bst_inorder_iter, bst_successor, bst_predecessor

def get_sample_bst(n):
    l = list(range(n))
    random.shuffle(l)
    return bst_create(l)

def test_bst_create():
    bst = get_sample_bst(10)
    l = list(range(10))
    l1 = bst_inorder(bst)
    assert len(l) == len(l1)
    for i, j in zip(l, l1):
        assert i == j

def test_bst_search():
    bst = get_sample_bst(20)
    n1 = bst_search(bst, 6)
    n2 = bst_search(bst, 100)
    assert n1.val == 6
    assert n2 == None

def test_bst_height():
    bst = get_sample_bst(20)
    lh = bst_height(bst.left)
    lr = bst_height(bst.right)
    h = bst_height(bst)

    assert h == 1 + max(lh, lr)

def test_inorder():
    bst = get_sample_bst(10)
    l1 = bst_inorder(bst)
    l2 = bst_inorder_iter(bst)
    assert len(l1) == len(l2)
    for i, j in zip(l1, l2):
        assert i == j

def test_dummy():
    bst = get_sample_bst(10)
    print(bst_inorder(bst))
    bst_inorder_iter(bst)

def test_successor():
    bst = get_sample_bst(30)
    res = bst_successor(bst, 13)
    assert res - 1 == 13

    bst = get_sample_bst(30)
    res = bst_successor(bst, 8)
    assert res - 1 == 8

    bst = get_sample_bst(30)
    res = bst_successor(bst, 5)
    assert res - 1 == 5

    bst = get_sample_bst(30)
    res = bst_successor(bst, 100)
    assert res == None


def test_predecessor():
    bst = get_sample_bst(30)
    res = bst_predecessor(bst, 13)
    assert res + 1 == 13

    bst = get_sample_bst(30)
    res = bst_predecessor(bst, 8)
    assert res + 1 == 8

    bst = get_sample_bst(30)
    res = bst_predecessor(bst, 5)
    assert res + 1 == 5

    bst = get_sample_bst(30)
    res = bst_predecessor(bst, -1)
    assert res == None
