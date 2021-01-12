# Create Weighted, directed edges

class WDE:
    # WDE from u to v
    def __init__(self, u : int, v : int, weight : float):
        self.u = u
        self.v = v
        self.weight = weight 

    def From(self) -> int:
        return self.u

    def To(self) -> int:
        return self.v

    def describe(self):
        return '{u} to {v}, {weight:.2f}\n'.format(u = self.u, v = self.v, weight = self.weight)
        


