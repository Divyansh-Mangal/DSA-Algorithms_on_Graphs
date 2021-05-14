#Uses python3
# Flight_paths => Breadth first search

import sys
from queue import Queue
import math

def bfs(adj, n, s, d):
    d[s][0] = 0
    d[s][1] = 1
    d[s][2] = d[0][0]%2

    q = Queue(maxsize = 0)
    q.put(s)

    while not q.empty():
        pro = q.get()
        for node in adj[pro]:
            if d[node][1] != 1:
                d[node][0] = d[pro][0] + 1
                d[node][1] = 1
                d[node][2] = d[node][0]%2
                q.put(node)
    return d

def isBipartite(adj, n, edges):
    d = []
    for _ in range(n):
        d.append([-1,0,None])

    for s in range(n):
        if d[s][2] == None:
            d = bfs(adj, n, s, d)

    bipartite = 1
    for a,b in edges:
        if d[a-1][2] == d[b-1][2]:
            bipartite = 0

    return bipartite

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]

    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    sys.setrecursionlimit(1000000)
    if n > 1:
        print(isBipartite(adj, n, edges))
    else:
        print(0)
