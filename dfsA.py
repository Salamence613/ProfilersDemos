import cProfile
import random

# An Iterative Python program to do DFS traversal from
# a given source vertex. DFS(int s) traverses vertices
# reachable from s.

# This class represents a directed graph using adjacency
# list representation


class Graph:
    def __init__(self, V):  # Constructor
        self.V = V  # No. of vertices
        self.adj = [[] for i in range(V)]  # adjacency lists

    def addEdge(self, v, w):  # to add an edge to graph
        self.adj[v].append(w)  # Add w to v’s list.

    # prints all not yet visited vertices reachable from s
    def initDFS(self, s):
        return [False for i in range(self.V)], [s]

    def popA(self, stack):
        return stack.pop(0)

    def pushA(self, stack, node):
        stack.insert(0, node)

    def DFS_A(self, s):  # prints all vertices in DFS manner from a given source.
        # Initially mark all vertices as not visited
        visited, stack = self.initDFS(s)

        while len(stack):
            # Pop a vertex from stack and print it
            s = self.popA(stack)

            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if not visited[s]:
                # print(s,end=' ')
                visited[s] = True

            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for node in self.adj[s]:
                if not visited[node]:
                    self.pushA(stack, node)


# Driver program to test methods of graph class
def main():
    g.DFS_A(0)


g = Graph(10000)
# Total 5 vertices in graph
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(1, 4)
for i in range(200000):
    g.addEdge(random.randrange(10000), random.randrange(10000))

print("Following is Depth First Traversal")
cProfile.run("main()", filename="dfsA.prof")
