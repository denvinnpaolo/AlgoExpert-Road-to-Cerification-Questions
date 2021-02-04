# Remove Duplicates From Linked List
# Easy
# Linked List

# Solution:

def RemoveDuplicateFromLinkedList(linkedList):
    cur = linkedList

    while cur:
        while cur.next and cur.value == cur.next.value:
            cur.next = cur.next.next
        cur = cur.next

    return linkedList