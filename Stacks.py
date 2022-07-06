class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def __str__(self):
        node = self.head
        values = [str(x.value) for x in self]
        return '\n'.join(values)
    def empty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self, value):
        node = Node(value)
        if self.empty():
            self.head = node
            node.next = None
        else:
            node.next = self.head
            self.head = node
    def delete(self):
        if self.empty():
            print('Already kuch nahi hai andhar')
        else:
            self.head = None
    def pop(self):
        if self.empty():
            return 'Kuch bhi nahi hai ismain toh'
        else:
            node = self.head.value
            self.head = self.head.next
            return print(node)
    def peek(self):
        if self.empty():
            return 'Kuch bhi nahi hai ismain toh'
        else:
            return self.head.value
s = Stack()
s.empty()
print(s.push(22))
s.push(29)
s.push(21)
s.push(1)
print(s)
s.pop()
print(s.peek())
s.delete()
print(s.peek())