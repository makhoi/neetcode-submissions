class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for c in tokens: 
            if c not in operators: 
                stack.append(int(c))
            else: 
                if c == '+':
                    num1 = stack[-1]
                    num2 = stack[-2]
                    total = num2 + num1
                    stack.pop()
                    stack.pop()
                    stack.append(total)
                elif c == '-':
                    num1 = stack[-1]
                    num2 = stack[-2]
                    difference = num2 - num1 
                    stack.pop()
                    stack.pop()
                    stack.append(difference)
                elif c == '*':
                    num1 = stack[-1]
                    num2 = stack[-2]
                    product = num2 * num1 
                    stack.pop()
                    stack.pop()
                    stack.append(product)
                elif c == '/':
                    num1 = stack[-1]
                    num2 = stack[-2]
                    quotient = int(num2 / num1)
                    stack.pop()
                    stack.pop()
                    stack.append(quotient)
        return stack[-1]