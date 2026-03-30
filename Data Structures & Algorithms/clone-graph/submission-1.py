"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            # if node is null
            if not node:
                return None
            # if node is already in the hashmap, we do not need to clone the node and just return the node
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            # add the copy to our hashmap
            oldToNew[node] = copy

            # make copies our every single neighbor of original node
            for nei in node.neighbors:
                # cloning the neighbors
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)

        

