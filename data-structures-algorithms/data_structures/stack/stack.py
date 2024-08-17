class Stack:
    def __init__(self):
        self.stack = []  # store stack elements

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    my_stack = Stack()
    # Pushing elements onto the stack
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    # Peeking at the top element
    print(f"Top element is: {my_stack.peek()}")  # Should print 30

    # Popping elements from the stack
    my_stack.pop()  # Should remove 30
    my_stack.pop()  # Should remove 20

    # Checking if the stack is empty
    print(f"Is the stack empty? {my_stack.is_empty()}")  # Should print False

    # Popping the last element
    my_stack.pop()  # Should remove 10

    # Checking if the stack is empty now
    print(f"Is the stack empty? {my_stack.is_empty()}")  # Should print True
