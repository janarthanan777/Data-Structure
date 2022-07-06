class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' | '.join(values)
    def empty(self):
        if self.head == None:
            return True
        else:
            return False
    def enqueue(self, value):
        node = Node(value)
        if self.empty():
            self.head = node
            node.next = None
            self.tail = node
        else:
            self.tail.next = node
            node.next = None
            self.tail = node
    def dequeue(self):
        if self.empty():
            print('Ulla onnume illa da')
        else:
            print(self.head.value)
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
    def peek(self):
        if self.empty():
            print('Ulla onnume illa da enna paakura')
        else:
            print(self.head.value)
    def delete(self):
        self.head = None
        self.tail = None
q = Queue()
q.enqueue(10)
q.enqueue(14)
q.enqueue(15)
q.dequeue()
print(q.empty())
print(q)
print(q.peek())