class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        return self.stack[-1] if self.stack else None
