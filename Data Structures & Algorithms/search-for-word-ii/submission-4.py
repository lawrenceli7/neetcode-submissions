class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        res = set()
        visit = set()

        def dfs(r, c, word, node):
            if (r < 0 or c < 0 or r >= rows or
            c >= cols or (r, c) in visit or
            board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endOfWord:
                res.add(word)

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col, word, node)

            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "", root)
        return list(res)
                   








