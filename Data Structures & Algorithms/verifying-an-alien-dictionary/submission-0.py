class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderIndex = {c:i for i, c in enumerate(order)}        
            # this is necessary
            # basically the order string is of no use...this hashmap is of use..which tells us the order of characters

        # verify adjacent words
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                # basically this condition is that before finding any different character in 2 strings..if word2 gets finished...meaning word2 is a prefix of word1...this means that the word1 and word2 are not in sorted order

                # we just rwant to compare the first mismatch character thats it
                if orderIndex[w1[j]] != orderIndex[w2[j]]:
                    if orderIndex[w1[j]] > orderIndex[w2[j]]:
                        return False

                    break
        
        return True