class Node:
    def __init__(self, value = None):
        self.next = None
        self.prev = None
        self.value = value
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        local = self.head
        while local:
            yield local
            local = local.next
    def insertDLL(self, value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
            else:
                temp = self.head
                count = 0
                while count < location - 1:
                    count += 1
                    temp = temp.next
                newNode.next = temp.next
                newNode.prev = temp
                temp.next.prev = newNode
                temp.next = newNode
                if temp == self.tail:
                    self.tail = newNode
    def traversallDLL(self):
        if self.head == None:
            print('There is no list to traverse')
        else:
            temp = self.head
            while temp:
                print(temp.value)
                if temp.next == None:
                    break
                else:
                    temp = temp.next
    def reverseTraversalDLL(self):
        if self.head is None:
            print('There is nothing to traverse boy')
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                temp = temp.prev
    def deleteNode(self, location):
        if self.head == None:
            print('There is no node to delete')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                index = 0
                temp = self.head
                while index < location - 1:
                    temp = temp.next
                    index += 1
                temp.next = temp.next.next
                temp.next.prev = temp
                if temp == self.tail:
                    temp = self.tail


doublell = DLL()
node1 = Node(23)
node2 = Node(24)
doublell.head = node1
doublell.tail = node2
doublell.head.next = node2
doublell.tail.prev = node1
doublell.insertDLL(29,0)
doublell.insertDLL(9,2)
doublell.insertDLL(2,3)
doublell.insertDLL(99,-1)
doublell.traversallDLL()
doublell.reverseTraversalDLL()
doublell.deleteNode(-1)
print([node.value for node in doublell])