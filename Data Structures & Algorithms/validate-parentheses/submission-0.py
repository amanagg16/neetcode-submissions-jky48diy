class Solution:
    def isValid(self, s: str) -> bool:
        match_last_bracket = []

        for char in s:
            if char in ["(", "[", "{"]:
                match_last_bracket.append(char)
            elif char in [")", "}", "]"]:
                if char == ")" and match_last_bracket[-1] == "(":
                    match_last_bracket.pop()
                elif char == "}" and match_last_bracket[-1] == "{":
                    match_last_bracket.pop()
                elif char == "]" and match_last_bracket[-1] == "[":
                    match_last_bracket.pop()
                else: return False

        return True if len(match_last_bracket) == 0 else False