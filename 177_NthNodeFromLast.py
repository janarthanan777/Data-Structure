from LinkedListForAllTypes import LinkedList
def nth(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head
    for i in range(n):
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1.value
ll = LinkedList()
print(ll.generate(10, 10, 0))
print(nth(ll, 3))