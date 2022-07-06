from LinkedListForAllTypes import LinkedList
def inter(ll1, ll2):
    node1 = ll1.head
    node2 = ll2.head
    node = 20
    if ll1.tail.value == ll2.tail.value:
        if len(ll1) != len(ll2):
            if len(ll1) > len(ll2):
                while len(ll1) > len(ll2):
                    node1 = node1.next
            else:
                while len(ll2) > len(ll1):
                    node2 = node2.next
        else:
            while node1:
                if node1.value == node2.value:
                    node = node1.value
                    while node1:
                        if node1.value != node2.value:
                            node = None
                            break
                        node1 = node1.next
                        node2 = node2.next
                else:
                    node1 = node1.next
                    node2 = node2.next


    return node
l1 = LinkedList()
l2 = LinkedList()
l1.add(2)
l1.add(8)
l1.add(3)
l1.add(9)
l1.add(4)
l2.add(7)
l2.add(8)
l2.add(3)
l2.add(9)
l2.add(4)
print(l1)
print(l2)
print(inter(l1, l2))