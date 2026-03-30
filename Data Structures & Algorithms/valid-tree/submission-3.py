class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # T, S: O(v + e)
        # adj list -> node with list of its neighbors
        # union find, if union return false, 
        # loop exists, at end size must equal n, 
        # or its not connected; dfs to get size 
        # and check for loop, since each edge is double, 
        # before dfs on neighbor of N, remove N from neighbor list of neighbor;

        if n == 0:
            return True

        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)

        



























