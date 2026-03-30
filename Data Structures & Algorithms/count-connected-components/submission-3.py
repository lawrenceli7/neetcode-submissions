class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # A set to keep track of visited nodes
        visit = set()

        def dfs(node):
            # Mark the node as visited
            visit.add(node)
            # Visit all the neighbors
            for neighbor in adj[node]:
                if neighbor not in visit:
                    dfs(neighbor)

        # Counter for the number of connected components
        components = 0

        # Iterate through all nodes
        for i in range(n):
            if i not in visit:
                # If a node hasn't been visited, it's a new component
                dfs(i)
                components += 1

        return components
        