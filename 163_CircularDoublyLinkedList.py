class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break
    def insertCDLL(self, value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.head.next = newNode
            self.head.prev = newNode
        else:
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                newNode.next = temp.next
                newNode.prev = temp
                temp.next.prev = newNode
                temp.next = newNode
    def reverseCDLL(self):
        temp = self.tail
        while temp:
            print(temp.value)
            if temp == self.head:
                break
            temp = temp.prev

CDLL = CircularDoublyLinkedList()
CDLL.insertCDLL(25,1)
CDLL.insertCDLL(222,0)
CDLL.insertCDLL(95,1)
CDLL.insertCDLL(1,1)
print([node.value for node in CDLL])
CDLL.reverseCDLL()