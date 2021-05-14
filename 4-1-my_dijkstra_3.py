#python3
#Dikstra 3

import math, sys
from heapq import heappush, heappop, heapify

def parent(i):
    return math.floor((i-1)/2)


def siftUp(heap,node):
    d = node[0]
    n = node[2]
    i = heap.index(node)

    while i > 0 and node[0] < heap[parent(i)][0]:
        swap = heap[i]
        heap[i] = heap[parent(i)]
        heap[parent(i)] = swap
        i = parent(i)

    return heap


def Dijkstra(adj, n, s ,t , edges):
    if s == t:
        return 0

    dist = {}
    prev = []


    for node in range(n):
        dist[node] = 1000000000
        prev.append(None)
    dist[s] = 0

    heap = []
    heapify(heap)

    count = 0
    for node in range(n):
        heappush(heap,(dist[node], count, node))

        count += 1

    while heap != []:
        u = heappop(heap)[2]

        for v in adj[u]:

            if dist[v] > dist[u] + edges[(u,v)]:
                pre_dist = dist[v]
                dist[v] = dist[u] + edges[(u,v)]

                heap[heap.index((pre_dist, v, v))] = (dist[v], v, v)
                heap = siftUp(heap, (dist[v], v, v))
                #heappush(heap, (dist[v], v, v))
                prev[v] = u

    return dist[t]

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n, m = data[0:2]

    if m>0:
        data = data[2:]

        edges = {}
        for e in range(m):
            edges[(data[3*e]-1, data[3*e + 1]-1)] = data[3*e + 2]

        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a].append(b)

        s,t = data[-2]-1, data[-1]-1
        sys.setrecursionlimit(1000000)

        answer = Dijkstra(adj, n, s,t, edges)

        if answer != 1000000000:
            print(answer)
        else:
            print(-1)
    else:
        print(-1)
