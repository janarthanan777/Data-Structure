# first we create a node class to create a node object with address to next variable(as NONE) and a value
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield (node.value)
            if node.next == self.head:
                break
            node = node.next

    def insertCLL(self, value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
                newNode.next = self.head
            else:
                temp = self.head
                count = 0
                while count < location - 1:
                    temp = temp.next
                    count += 1
                newNode.next = temp.next
                temp.next = newNode
                if temp == self.tail:
                    self.tail = newNode

    def traversalCSLL(self):
        if self.head == None:
            print('It is an empty list')
        else:
            node = self.head
            ode = self.head
            while node is not None:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break

    def deleteCSLL(self, location):
        if self.head == None:
            print('There is no CSLL')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    while True:
                        if temp.next == self.tail:
                            break
                        temp = temp.next
                    temp.next = self.tail.next
                    self.tail = temp
            else:
                temp = self.head
                count = 0
                while count < location - 1:
                    temp = temp.next
                    count += 1
                temp.next = temp.next.next


circularLL = CLL()
node1 = Node(1)
node2 = Node(2)
circularLL.head = node1
circularLL.head.next = node2
circularLL.tail = node2
circularLL.insertCLL(4, 1)
circularLL.insertCLL(99, 0)
circularLL.insertCLL(4, 0)
circularLL.insertCLL(99, 0)
print([node for node in circularLL])
circularLL.deleteCSLL(4)
circularLL.traversalCSLL()
