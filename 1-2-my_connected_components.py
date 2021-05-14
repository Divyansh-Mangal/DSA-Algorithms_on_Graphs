#python3
#Reachability of graphs
#implementing a graph vertex using adjacency List

import sys

class Vertex():
    def __init__(self, value, visited = False):
        self.value = value
        self.visited = False
        self.CCnum = None
        self.N = []                        #Neighbours

def Explore(u, cc):
    u.visited = True
    CCnum = cc
    for n in u.N:
        if not n.visited:
            Explore(n, cc)
    return

def DFS(nodes):
    cc = 0
    for u in nodes:
        if not u.visited:
            Explore(u, cc)
            cc += 1
    return cc

def CC(n, vertices):
    nodes = []

    for v in range(n):
        nodes.append(Vertex(v+1))

    i = 0
    while i < len(vertices):
        a = vertices[i]
        i += 1
        b = vertices[i]

        for n in nodes:
            if n.value == a:
                a = n
            if n.value == b:
                b = n
        if b not in a.N:
            a.N.append(b)
        if a not in b.N:
            b.N.append(a)
        i += 1

    return DFS(nodes)


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n = data[0]
    m = data[1]
    vertices = data[2::]
    
    print(CC(n, vertices))
