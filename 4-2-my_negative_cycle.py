#python3
# Negetive Weight cycles detection
import sys, math

def DetectNegCycles(adj, n, edges):
    negCycle = 0
    dist = []
    prev = []
    for _ in range(n):
        dist.append(1001)
        prev.append(None)

    visited = []

    cycles = 1
    while cycles <= n-1:
        relaxed = 0
        for u in edges:
            if dist[u[1]] > dist[u[0]] + edges[u]:
                dist[u[1]] = dist[u[0]] + edges[u]
                relaxed += 1
        if relaxed == 0:
            break
        else:
            cycles += 1

    if cycles == n:
        relaxed = 0
        for u in edges:
            if dist[u[1]] > dist[u[0]] + edges[u]:
                dist[u[1]] = dist[u[0]] + edges[u]
                relaxed += 1

    if cycles == n and relaxed > 0:
        negCycle = 1

    return negCycle

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]

    edges = {}
    for e in range(m):
        edges[(data[3*e]-1, data[3*e + 1]-1)] = data[3*e + 2]

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a].append(b)

    sys.setrecursionlimit(1000000)

    print(DetectNegCycles(adj, n, edges))
