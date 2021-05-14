#Uses python3
# Flight_paths => Breadth first search

import sys
from queue import Queue
import math

def distance(adj, s, t, n):
    d = []
    for _ in range(n):
        d.append([-1,0])

    d[s][0] = 0
    d[s][1] = 1

    q = Queue(maxsize = 0)
    q.put(s)

    while not q.empty():
        pro = q.get()
        for node in adj[pro]:
            if d[node][1] != 1:
                d[node][1] = 1
                d[node][0] = d[pro][0] + 1
                q.put(node)

    return d[t][0]

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

    s, t = data[2 * m] - 1, data[2 * m + 1] - 1

    sys.setrecursionlimit(1000000)

    print(distance(adj, s, t, n))
