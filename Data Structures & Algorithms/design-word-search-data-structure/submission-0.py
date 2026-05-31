class TrieNode:
    def __init__(self, endWord=False):
        self.endWord = endWord
        self.children = 26*[None]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None:
                current.children[index] = TrieNode()

            current = current.children[index]
        
        current.endWord = True

    def search(self, word: str) -> bool:
        
        def dfs(word, index, current):
            if index == len(word):
                return current.endWord

            if word[index] == '.':
                for i in range(0, 26):
                    if current.children[i] is not None and dfs(word, index+1, current.children[i]):
                        return True
                        
            else:
                i = ord(word[index]) - ord('a')
                if current.children[i] is not None and dfs(word, index+1, current.children[i]):
                    return True
                
            return False
        
        return dfs(word, 0, self.root)