class Stack:
    def __init__(self) -> None:
        self.items = []

    def peek(self):
        return self.items[-1]

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0


if __name__ == '__main__':
    stack = Stack()
    assert stack.isEmpty() == True
    stack.push(10)
    assert stack.peek() == 10
    assert stack.isEmpty() == False
    stack.push(20)
    assert stack.size() == 2
    stack.pop()
    stack.pop()
    assert stack.isEmpty() == True
