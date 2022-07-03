from LinkedListForAllTypes import LinkedList
def removeDup(ll):
    current = ll.head
    list = [current.value]
    while current.next:
        if current.next.value in list:
            current.next = current.next.next
        else:
            list.append(current.value)
            current = current.next
 #   return ll
lll = LinkedList()
print(lll.generate(10, 10, 1))
removeDup(lll)
print(lll)
#print(lll)
