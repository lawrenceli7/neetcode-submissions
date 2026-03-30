class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time, Space: O(v + e)
        # union find, if union return false, 
        # loop exists, at end size must equal n, 
        # or its not connected; dfs to get size 
        # and check for loop, since each edge is double, 
        # before dfs on neighbor of N, remove N from neighbor list of neighbor;

        if not n:
            return True
        
        visit = set()
        adj = {i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)



























