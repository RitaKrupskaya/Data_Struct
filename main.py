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


n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
print(n2.next_node)


