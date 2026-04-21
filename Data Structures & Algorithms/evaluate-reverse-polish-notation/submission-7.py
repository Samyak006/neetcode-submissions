class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "*-+/"
        stack = []
        def calculate(a,b,op):
            if op == "*":
                return a*b
            if op == "/":
                return int(float(a)/b)
            if op == "+":
                return a+b
            if op == "-":
                return a-b
        
        for i in tokens:
            if not stack:
                stack.append(int(i))
            else:
                if i in ops:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(calculate(b,a,i))
                else:
                    stack.append(int(i))
        return stack[0]