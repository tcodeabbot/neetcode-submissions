class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in {'+', '-', '*', '/'}:
                stack.append(int(c))
            else:
                second = stack.pop()
                first = stack.pop()

                if c == '+':
                    result = first + second
                elif c == '-':
                    result = first - second
                elif c == '*':
                    result = first * second
                else:
                    result = int(first / second)
                stack.append(result)
        
        return stack[-1]