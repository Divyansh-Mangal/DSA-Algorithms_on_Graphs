#python3
import sys, math

class Disjoint_set():
    def __init__(self):
        self.parent = []
        self.rank = []

    def __str__(self):
        return f'{list(range(len(self.parent)))}\n{self.parent}=parent\n{self.rank}=rank'

    def MakeSet(self,i):
        self.parent.append(i)
        self.rank.append(0)

    def Find(self,i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def Union(self,i,j):
        i_p = self.Find(i)
        j_p = self.Find(j)
        if i_p == j_p:
            return
        if self.rank[i_p] > self.rank[j_p]:
            self.parent[j_p] = i_p
        else:
            self.parent[i_p] = j_p
            if self.rank[i_p] == self.rank[j_p]:
                self.rank[j_p] += 1

    def Union_PC(self,i,j):
        i_p = self.Find_PC(i)
        j_p = self.Find_PC(j)
        if i_p == j_p:
            return
        if self.rank[i_p] > self.rank[j_p]:
            self.parent[j_p] = i_p
        else:
            self.parent[i_p] = j_p
            if self.rank[i_p] == self.rank[j_p]:
                self.rank[j_p] += 1

    def Find_PC(self,i):
        if i != self.parent[i]:
            self.parent[i] = self.Find_PC(self.parent[i])
        return self.parent[i]


def mST(edges, nodes, n, k):
    cost = []
    for i in range(n):
        cost.append([math.inf,0])
    cost[0] = [0,1]

    nodeset = Disjoint_set()
    for i in range(n):
        nodeset.MakeSet(i)

    pathLen = [0]*k
    pathLen.sort()
    while len(set(nodeset.parent)) > 1:
        e = min(edges.keys())
        for a in edges[e]:
            if nodeset.Find_PC(a[0]) != nodeset.Find_PC(a[1]):
                nodeset.Union(a[0], a[1])
                if e > pathLen[0]:
                    pathLen[0] = e
                    pathLen.sort()
        del edges[e]

    return pathLen[1]


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    #@GEwXQ8wxCvt6j3
    n = data[0]
    data = data[1::]
    xs = data[0::2]
    ys = data[1::2]
    k = data[-1]
    nodes = {}
    for i in range(n):
        nodes[i] = (xs[i], ys[i])

    edges = {}
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            length = math.sqrt((nodes[i][0] - nodes[j][0])**2 + (nodes[i][1] - nodes[j][1])**2)
            if length not in list(edges.keys()):
                edges[length] = []
            edges[length].append((i,j))

    if n > 1:
        pass
        print('{0:.9f}'.format(mST(edges, nodes, n, k)))
    else:
        print(0)
