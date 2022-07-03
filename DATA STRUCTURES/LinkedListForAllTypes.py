import random
class Node:
    def __init__(self, values = None):
        self.value = values
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)
    def __len__(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count
    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    def generate(self, n, max, min):
        for i in range(n):
            self.add(random.randint(min, max))
        return self
ll = LinkedList()
print(ll.generate(10, 100, 1))
