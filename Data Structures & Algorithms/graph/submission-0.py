class Graph:
    
    def __init__(self):
        # Dictionary to store adjacency list: {node: {neighbors}}
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        # If nodes don't exist, initialize them with empty sets
        if src not in self.adj:
            self.adj[src] = set()
        if dst not in self.adj:
            self.adj[dst] = set()

        # Add the directed edge
        self.adj[src].add(dst)    
  
    def removeEdge(self, src: int, dst: int) -> bool:
        # If src doesn't exist or dst isn't a neighbor of src
        if src not in self.adj or dst not in self.adj[src]:
            return False
        
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        # Helper function for DFS
        def dfs(curr, target, visited):
            if curr == target:
                return True
            
            visited.add(curr)

            # Explore neighbors
            for neighbor in self.adj.get(curr, []):
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False

        return dfs(src, dst, set())
