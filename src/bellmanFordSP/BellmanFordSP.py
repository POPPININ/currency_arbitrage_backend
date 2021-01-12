from .EdgeWeightedDigraph import EdgeWeightedDigraph
from .EdgeWeightedDirectedCycle import EdgeWeightedDirectedCycle
import math

class BellmanFordSP:

    # find shortest paths from vertex v to all other vertices in G
    def __init__(self, G : EdgeWeightedDigraph, v : int):
        self.G = G
        self.distTo = [math.inf] * G.V # length of paths from v to other vertices
        self.edgeTo = [None] * G.V # last edge on path to v
        self.onQ = [False] * G.V # Is this vertex on the queue?
        self.queue = [] # vertices to relax
        self.cycle = [] # list of vertices (in order) in cycle, if any
        self.cost = 0 # number of calls to relax

        # Bellman-Ford algorithm
        self.distTo[v] = 0.0
        self.queue.append(v)
        self.onQ[v] = True

    # Does the input Digraph have a negative cycle?
    def hasNegativeCycle(self) -> bool:
        return (len(self.cycle) > 0)

    def initializeSPsearch(self):
        # search for shortest paths until negative cycle is not found
        while(len(self.queue) > 0 and not self.hasNegativeCycle()):
            w = self.queue.pop(0)
            self.onQ[w] = False
            self.relax(self.G, w)
    
    # relax vertex s
    def relax(self, G : EdgeWeightedDigraph, s : int):
        for e in G.adjacencyList[s]:
            w = e.To()

            # Does triangle inequality hold?
            if(self.distTo[w] > self.distTo[s] + e.weight):
                self.distTo[w] = self.distTo[s] + e.weight
                self.edgeTo[w] = e
                if not self.onQ[w]:
                    self.queue.append(w)
                    self.onQ[w] = True
            
            # find negative cycle if all vertices have been relaxed
            self.cost += 1
            if(self.cost % G.V == 0):
                self.findNegativeCycle()
                if(self.hasNegativeCycle()):
                     return

    # finds Negative Cycle, if any.
    def findNegativeCycle(self) -> list:
        V = len(self.edgeTo)
        spt = EdgeWeightedDigraph(V) # Initialize Digraph to find shortest path
        for i in range(V):
            if(self.edgeTo[i] != None): # Is there an edge from v to i?
                spt.addEdge(self.edgeTo[i])

        # Find cycle using dfs
        cycleFinder = EdgeWeightedDirectedCycle(spt)
        cycleFinder.initializeDfs()
        self.cycle = cycleFinder.cycle

    # return vertices in path from v to s
    def pathTo(self, s : int) -> list:
        if(self.hasNegativeCycle()):
            # throw error
             print("Unsupported Operation!")
             return 
        if(not self.hasPathTo(s)):
            print('There does not exist a path to {s}'.format(s = s))
            return 

        path = [] # treat as stack

        e = self.edgeTo[s]
        while(e != None):
            path.append(e)
            e = self.edgeTo[e.From()]
        
        return path
    
    # Is there a directed path from v to s?
    def hasPathTo(self, s : int) -> bool:
        return self.distTo[s] < math.inf
    
    # return distance from v to s
    def distTo(self, s : int) -> float:
        if(hasNegativeCycle()):
            print('Unsupported Operation!')
            return
        else:
            return self.distTo[s]
    
    # return negative cycle, if any.
    def negativeCycle(self) -> list: 
        return self.cycle 
