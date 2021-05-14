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

def Explore(u):
    u.visited = True
    for n in u.N:
        if not n.visited:
            Explore(n)
    return

def exitMaze(n, vertices, uv):
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

    v = uv[0]
    u = uv[1]

    for n in nodes:
        if n.value == u:
            u = n

        if n.value == v:
            v = n

    Explore(u)

    if v.visited == True:
        return 1
    else:
        return 0


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n = data[0]
    m = data[1]
    vertices = data[2:len(data)-2:]
    uv = data[:-3:-1]

    if n == 0 or m==0:
        print(0)
    else:
        print(exitMaze(n, vertices, uv))
