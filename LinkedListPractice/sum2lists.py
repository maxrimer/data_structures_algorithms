from LinkedListClass import LinkedList


def sum_two_lists(ll1, ll2):
    num1 = ll1.head
    num2 = ll2.head
    carry = 0
    new_ll = LinkedList()

    while num1 or num2:
        result = carry
        if num1:
            result += num1.value
            num1 = num1.next
        if num2:
            result += num2.value
            num2 = num2.next
        new_ll.add(int(result % 10))
        carry = int(result // 10)

    return new_ll


llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)

llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)

print(llA)
print(llB)
print(sum_two_lists(llA, llB))