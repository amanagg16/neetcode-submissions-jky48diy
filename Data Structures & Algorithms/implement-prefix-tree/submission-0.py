class TrieNode:
    def __init__(self, wordEnd=False):
        self.children = 26*[None]
        self.wordEnd = wordEnd
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode() 
            
            current = current.children[index]
        
        current.wordEnd = True
            


    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not current.children[index]:
                return False
        
            current = current.children[index]
            
        return True if current.wordEnd else False



    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not current.children[index]:
                return False
        
            current = current.children[index]
            
        return True
        
        