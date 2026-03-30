class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # adjacency list -> node with list of its neighbors
        # no cycles/loops and must be connected
        # number of visited node == number of nodes given to us
        # need "prev" to check what the previous node was, so we do not need to go back to the node we visited

        if not n:
            return True

        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)

            # check every neighbor of node
            for nei in adj[node]:
                if nei == prev:
                    continue
                # detected a cycle
                if not dfs(nei, node):
                    return False
            return True
                                # graph is connected
        return dfs(0, -1) and n == len(visit)

        



























