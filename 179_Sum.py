from LinkedListForAllTypes import LinkedList
def sum(ll1, ll2):
    node1 = ll1.head
    node2 = ll2.head
    num1, num2, a, b, c, d = 0, 0, 0, 0, 0, 0
    while node1:
        c = node1.value * 10**a
        num1 = num1 + c
        a = a + 1
        node1 = node1.next
    while node2:
        d = node2.value * 10**b
        b = b + 1
        num2 = num2 + d
        node2 = node2.next
    sum = num1 + num2
    return sum
lll1 = LinkedList()
lll2 = LinkedList()
lll1.generate(3, 9, 1)
lll2.generate(3, 9, 1)
print(lll1)
print(lll2)
print(sum(lll1, lll2))

