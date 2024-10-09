class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def count(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Số phần tử trên ngăn xếp:", stack.count())  
stack.pop()
print("Số phần tử trên ngăn xếp sau khi pop:", stack.count())  
