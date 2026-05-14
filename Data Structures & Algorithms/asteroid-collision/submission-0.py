class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        i=0
        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                if(abs(stack[-1])>abs(i)):
                    i = 0
                elif(abs(stack[-1])<abs(i)):
                    stack.pop()
                else:
                    i = 0
                    stack.pop()
            if i:
                stack.append(i)
        return stack

