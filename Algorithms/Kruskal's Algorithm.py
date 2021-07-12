# Kruskal's minimum spanning tree algorithm is used to find the the spanning tree of a graph.
# A spanning tree of a graph is a subgraph that is a tree and connects all of the vertecies together.
# A minimum spanning tree is form of a weighted, connected, and undirected graph is one with weight less than or equal to the weight of every spanning tree.
#   Go Here to learn more about spanning trees, MST, and Kruskal's algorithm: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/?ref=lbp

# Kruskal's algorithm has three main steps:
    # 1) Sort all edges in non-decreasing order of their weight.
    # 2) Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
    # 3) Repeat step 2 until there are V-1 edges in the spanning tree, where V is the number of vertecies in a given graph

import 