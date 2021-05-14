#python3
#Reachability of graphs
#implementing a graph vertex using adjacency List

import sys

class Vertex():
    def __init__(self, value, visited = False):
        self.value = value
        self.visited = False
        self.CCnum = None
        self.N = []                   #Neighbours
        self.preOrder = None
        self.postOrder = None

    def __str__(self):
        string = f'v = {self.value}, visit = {self.visited}, neighbours = '
        for n in self.N:
            string = string + f'{n.value}, '

        return string

def Explore(u, visited):
    visited[u] = True

    for n in adj[u]:
        if not visited[n]:
            visited = Explore(n, visited)

    print(u+1, end = " ")

    return visited

def DFS(adj, visited):
    i = 0
    while i < len(adj):
        if not visited[i]:
            Explore(i, visited)
        i+=1
    return

def  topoSort(adj):
    visited = [False]*len(adj)
    DFS(adj, visited)

    return


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]

    for (a, b) in edges:
        adj[b - 1].append(a - 1)

    sys.setrecursionlimit(1000000)

    topoSort(adj)
