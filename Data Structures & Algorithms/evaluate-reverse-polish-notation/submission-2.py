class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []

        for i in range(len(tokens)):
            if(tokens[i] in ['+', '-', '*', '/']):
                b = stack.pop()
                a = stack.pop()
                if(tokens[i]=='+'):
                    stack.append(a+b)
                elif(tokens[i]=='-'):
                    stack.append(a-b)
                elif(tokens[i]=='*'):
                    stack.append(a*b)
                elif(tokens[i]=='/'):
                    stack.append(int(a/b))
            
            else:
                stack.append(int(tokens[i]))
        return int(stack[-1])