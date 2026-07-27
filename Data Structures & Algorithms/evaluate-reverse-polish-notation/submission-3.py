class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+","-","*","/"}
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                x = stack.pop()
                y = stack.pop()
                stack.append(str(math.trunc(eval(y + t + x))))
        return int(stack[-1])