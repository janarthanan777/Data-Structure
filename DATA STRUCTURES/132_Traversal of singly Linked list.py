class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
#insertion in linked list
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                newNode.next = None
                self.tail = newNode
            else:
                temp = self.head
                index = 0
                while index < (location - 1):
                    temp = temp.next
                    index += 1
                newNode.next = temp.next
                temp.next = newNode
                if temp == self.tail:
                    self.tail = newNode
### Traversal in CLL
    def traversal(self):
        if self.head is None:
            print('The list is empty')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
## search for a node in CLL
    def searchSLL(self, NodeValue):
        if self.head is None:
            print('There are no values in here, i.e the list is empty')
        else:
            count = 0
            node = self.head
            while node is not None:
                if node.value == NodeValue:
                    return 'Value found mutherfucker,  at index {}'.format(count)
                count = count + 1
                node = node.next
            return 'The value was not to be found'
###delete a node from CLL
    def delSLL(self, location):
        if self.head == None:
            print('The list has always been empty')
        else:
            if location == 0:
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                temp = self.head
                count = 0
                while count < location:
                    temp = temp.next
                    count = count +1
                nex = temp.next
                temp.next = nex.next
####DELETION OF ENTIRE SINGLY LINKED LIST
    def deleteEntireSLL(self):
        if self.head is None:
            print('CLL does not exist')
        else:
            self.head = None
            self.tail = None



sLinkedList = SinglyLinkedList()
sLinkedList.insertSLL(2, 4)
sLinkedList.insertSLL(5, 0)
sLinkedList.insertSLL(4, 1)
print([node.value for node in sLinkedList])
sLinkedList.delSLL(1)
sLinkedList.traversal()
print(sLinkedList.searchSLL(4))
