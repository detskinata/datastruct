class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node



class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(data=value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        remove = self.top
        if self.top is None:
            return None
        self.top = self.top.next_node
        return remove.data


stack = Stack()
stack.push('data1')
data = stack.pop()

print(stack.top)
print(data)

stack = Stack()
stack.push('data1')
stack.push('data2')
