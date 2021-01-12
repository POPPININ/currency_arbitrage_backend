from .EdgeWeightedDigraph import EdgeWeightedDigraph 

# find a cycle, if any, in the given Digraph
class EdgeWeightedDirectedCycle:

    def __init__(self, G : EdgeWeightedDigraph):
        self.G = G
        self.marked = [False] * G.V
        self.onStack = [False] * G.V # Is edge v on cycle[]?
        self.edgeTo = [None] * G.V
        self.cycle = [] # stack of edges in the order they appear in the cycle

    def initializeDfs(self):
        for i in range(self.G.V):
            if not self.marked[i] :
                self.dfs(self.G, i)

    # Depth-first search to find cycle
    def dfs(self, G : EdgeWeightedDigraph, v : int):
        self.onStack[v] = True
        self.marked[v] = True

        for e in G.adjacencyList[v]: 
            w = e.To() # e is of type WDE

            # return if cycle already found
            if(len(self.cycle) > 0):
                 return

            if self.onStack[w]:
                temp = e
                while(temp.From() != w):
                    self.cycle.append(temp)
                    temp = self.edgeTo[temp.From()]
                self.cycle.append(temp)
                return 
            
            if not self.marked[w]:
                self.edgeTo[w] = e
                self.dfs(G, w)
        
        self.onStack[v] = False

    # Is there a cycle in this Digraph?
    def hasCycle(self) -> bool:
        return (len(self.cycle) > 0)


