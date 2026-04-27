class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            if (stack[-1] > 0 and asteroids[i] < 0) or (stack[-1] < 0 and asteroids[i] > 0):
                temp = stack.pop()
                if abs(temp) == abs(asteroids[i]):
                    continue
                stack.append(max(abs(temp), abs(asteroids[i])))
            else:
                stack.append(asteroids[i])
        
        return stack
