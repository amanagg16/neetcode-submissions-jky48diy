class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c in ['+','-','*','/']:
                if c == '+':
                    stack.append(stack.pop() + stack.pop())
                elif c == '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a-b)
                elif c == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a/b)
            else:
                stack.append(int(c))
            
        return stack.pop()