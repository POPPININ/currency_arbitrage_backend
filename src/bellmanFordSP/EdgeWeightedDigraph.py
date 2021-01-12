from .WDE import WDE
from collections import defaultdict

# Create Digraphs with weighted edges
class EdgeWeightedDigraph:

    def __init__(self, V):
        self.V = V  # number of vertices
        self.E = 0  # number of edges
        self.inDegree = [0]*V   # in-degrees of each vertex
        self.adjacencyList = defaultdict(list)  # adjacency list; return adjacencyList[k]
    
    def addEdge(self, edge : WDE):
        v = edge.From() # tail
        w = edge.To() # head
        self.adjacencyList[v].append(edge) # append edge originating from v
        self.inDegree[w] += 1 # increment w's in-degree
        self.E +=1 
    
    # return outDegree of vertex v
    def outDegree(self, v : int) -> int:
        return len(self.adjacencyList[v])
    
    # return a list of edges in the Digraph
    def edges(self) -> list:
        edges = []
        for adjList in self.adjacencyList:
            for edge in adjList:
                edges.append(edge)
        return edges


