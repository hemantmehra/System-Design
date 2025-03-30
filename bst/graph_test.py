from graph import graph_sample1, graph_topologial_sort, graph_sample2

def test_topological_sort():
    g = graph_sample1()
    l = graph_topologial_sort(g)
    assert len(l) == len(g)
    assert tuple(l) == (1, 2, 3, 4, 5, 7, 6)

    g = graph_sample2()
    l = graph_topologial_sort(g)
    assert len(l) == len(g)
    assert tuple(l) == (2, 1, 3, 4, 5)
