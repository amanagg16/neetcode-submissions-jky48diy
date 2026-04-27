class     Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                temp = stack.pop()
                if abs(temp) == abs(asteroids[i]):
                    asteroids[i] = 0
                    break
                elif abs(temp) > abs(asteroids[i]):
                    stack.append(temp)
                    asteroids[i] = 0
                    break
            
            if asteroids[i] != 0:
                stack.append(asteroids[i])
        
        return stack