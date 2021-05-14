#python3

# NEGETICE cYCLE CHECK FOR EXCHANGING MONEY

import sys, math

def exchangeMoney(adj, n, m, start, edges):
    dist = []
    updated = []
    for _ in range(n):
        dist.append(1000000001*m)
        updated.append(0)

    dist[start] = 0
    updated[start] = 1
    cycles = 1
    while True:
        relaxed = 0

        for u in edges:
            if dist[u[1]] > dist[u[0]] + edges[u] and updated[u[1]] < n:
                dist[u[1]] = dist[u[0]] + edges[u]
                updated[u[1]] += 1
                relaxed += 1

        if relaxed == 0:
            break
        else:
            cycles += 1

    answer = []
    for i in range(n):
        if updated[i] >= n:
            answer.append('-')
        elif 0 < updated[i] < n:
            answer.append(dist[i])
        elif updated[i] == 0:
            answer.append('*')

    return answer

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

    s = data[-1]-1

    sys.setrecursionlimit(1000000)

    result = exchangeMoney(adj, n, m, s, edges)

    for r in result:
        print(r)
