class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(2, 5)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(99, 0)
singlyLinkedList.insertSLL(4, 2)
print([node.value for node in singlyLinkedList])
