class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                x=float(stack.pop())
                y=float(stack.pop())
                z=x+y
                stack.append(str(z))
            elif char == '*':
                x=float(stack.pop())
                y=float(stack.pop())
                z=x*y
                stack.append(str(z))
            elif char == '-':
                x=float(stack.pop())
                y=float(stack.pop())
                z=y-x
                stack.append(str(z))
            elif char == '/':
                x=float(stack.pop())
                y=float(stack.pop())
                z=int(y/x)
                stack.append(str(z))
            else:
                stack.append(char)
        return int(float(stack[0]))