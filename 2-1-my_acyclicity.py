#python3
#Checking cyclicity of graph

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

def Explore(u, time, cycle):
    time += 1
    u.visited = True
    u.preOrder = time

    for n in u.N:
        if not n.visited:
            time, cycle = Explore(n, time, cycle)
        else:
            if n.postOrder == None and n.N != []:
                cycle = 1
    time += 1
    u.postOrder = time
    return time, cycle

def DFS(nodes):
    time = 0
    cycle = 0

    for u in nodes:
        if not u.visited:
            time, cycle = Explore(u, time, cycle)

    return cycle

def IsCyclic(n, vertices):
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

        i += 1

    return DFS(nodes)



if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n = data[0]
    m = data[1]
    vertices = data[2::]

    print(IsCyclic(n, vertices))
