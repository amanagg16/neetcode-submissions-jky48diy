class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        digits_to_letters = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        output = []
        n = len(digits)

        def backtrack(index, res):
            if index == n:
                output.append("".join(res))
                return
            
            current_letters = digits_to_letters[digits[index]]
            for i in range(len(current_letters)):
                res.append(current_letters[i])
                backtrack(index+1, res)
                res.pop()
        
        backtrack(0,[])
        return output