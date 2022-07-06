from LinkedListForAllTypes import LinkedList
def partition(ll, n):
    node = ll.head
    ll.tail = ll.head
    while node:
        nextNode = node.next
        if node.value < n:
            node.next = ll.head
            ll.head = node
        else:
            ll.tail.next = node
            ll.tail = node
            ll.tail.next = None
        node = nextNode
lll = LinkedList()
print(lll.generate(10, 10, 0))
partition(lll, 5)
print(lll)


