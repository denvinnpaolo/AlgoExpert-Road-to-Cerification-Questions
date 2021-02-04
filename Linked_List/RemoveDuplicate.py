# Remove Duplicates From Linked List
# Easy
# Linked List

# Solution:

def RemoveDuplicateFromLinkedList(linkedList):
    cur = linkedList
    # while cur is not None keep iterating
    while cur:
        # while there is a next node and current node value is equal to the value of the next node keep iterating
        while cur.next and cur.value == cur.next.value:
            # changes next value to the next of the next node
            cur.next = cur.next.next
        # makes the next node the current node
        cur = cur.next

    return linkedList

    