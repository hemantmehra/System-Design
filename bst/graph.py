
def graph_sample1():
    d = {}
    d[1] = [2]
    d[2] = [3]
    d[3] = [4]
    d[4] = [5]
    d[5] = [6, 7]
    d[6] = []
    d[7] = []
    return d

def graph_sample2():
    d = {}
    d[1] = [3, 4]
    d[2] = [3, 5]
    d[3] = [4]
    d[4] = [5]
    d[5] = []
    return d

def graph_topologial_sort(g):
    visited = set()
    stack = []

    def dfs(g, v):
        visited.add(v)

        for v1 in g[v]:
            if v1 not in visited:
                visited.add(v1)
                dfs(g, v1)
                stack.append(v1)

    k = list(g.keys())
    for i in g:
        if i not in visited:
            dfs(g, i)
            stack.append(i)

    l = []
    while stack:
        l.append(stack.pop())
    return l
