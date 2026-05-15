# Problem: Reverse Linked List
# Day: 16
# Time Complexity: O(n)

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):

    prev = None
    curr = head

    while curr:

        nxt = curr.next

        curr.next = prev

        prev = curr

        curr = nxt

    return prev


# create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# reverse list
newhead = reverse(head)

# print reversed list
while newhead:
    print(newhead.data, end=" -> ")
    newhead = newhead.next
