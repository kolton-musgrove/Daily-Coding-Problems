# A Depth First Search (DFS) can be used to traverse or search a graph or tree.
# The algorithm starts at the root node and traverses each branch as far as it can before backtracking
#   Go here for more information about DFS: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

# This implementation is used to detect a cycle in a graph. A cycle is basically a "loop" in a graph where A -> B -> ... -> A
# This algorithm is sourced from GeeksforGeeks: https://www.geeksforgeeks.org/detect-cycle-in-a-graph/?ref=lbp

# The algorithm has the following steps:
# 1) Create the graph using the given number of edges and vertices.
# 2) Create a recursive function that initializes the current index or vertex, visited, and recursion stack.
# 3) Mark the current node as visited and also mark the index in recursion stack.
# 4) Find all the vertices which are not visited and are adjacent to the current node.
#    Recursively call the function for those vertices, If the recursive function returns true, return true.
# 5) If the adjacent vertices are already marked in the recursion stack then return true.
# 6) Create a wrapper class, that calls the recursive function for all the vertices and if any function returns true return true.
#    Else if for all vertices the function returns false return false.

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")

# Thanks to Divyanshu Mehta for contributing this code