class StackSolutions:
    # 1. Valid Parentheses
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in Map:
                if stack and stack[-1] == Map[char]: stack.pop()
                else: return False
            else:
                stack.append(char)
        return True if not stack else False

    # 2. Simplify Path
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part == "..":
                if stack: stack.pop()
            elif part and part != ".":
                stack.append(part)
        return "/" + "/".join(stack)

    # 3. Min Stack
    class MinStack:
        def __init__(self):
            self.stack = []
            self.minStack = []
        def push(self, val: int) -> None:
            self.stack.append(val)
            val = min(val, self.minStack[-1] if self.minStack else val)
            self.minStack.append(val)
        def pop(self) -> None:
            self.stack.pop()
            self.minStack.pop()
        def top(self) -> int: return self.stack[-1]
        def getMin(self) -> int: return self.minStack[-1]

    # 4. Evaluate Reverse Polish Notation
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                b, a = stack.pop(), stack.pop()
                if t == "+": stack.append(a + b)
                elif t == "-": stack.append(a - b)
                elif t == "*": stack.append(a * b)
                else: stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[0]
