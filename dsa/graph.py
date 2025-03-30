
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

class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n+1))

    def find_parent(self, v):
        while v != self.parent[v]:
            v = self.parent[v]
        return v
    
    def union(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.rank[pu] += 1
            self.parent[pv] = pu
