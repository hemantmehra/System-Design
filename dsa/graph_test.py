from graph import graph_sample1, graph_topologial_sort, graph_sample2
from graph import DisjointSet

def test_topological_sort():
    g = graph_sample1()
    l = graph_topologial_sort(g)
    assert len(l) == len(g)
    assert tuple(l) == (1, 2, 3, 4, 5, 7, 6)

    g = graph_sample2()
    l = graph_topologial_sort(g)
    assert len(l) == len(g)
    assert tuple(l) == (2, 1, 3, 4, 5)

def test_disjoint_set():
    ds = DisjointSet(7)
    ds.union(1, 2)
    ds.union(2, 3)
    assert ds.find_parent(2) == ds.find_parent(3)

    ds.union(4, 5)
    ds.union(6, 7)
    ds.union(5, 6)
    assert ds.find_parent(7) == 4
    assert ds.find_parent(5) == ds.find_parent(7)

    ds.union(3, 7)
    assert ds.find_parent(2) == ds.find_parent(7)
