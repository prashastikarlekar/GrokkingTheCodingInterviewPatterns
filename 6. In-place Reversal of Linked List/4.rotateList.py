# https://leetcode.com/problems/rotate-list/

# Given the head of a linked list, rotate the list to the right by k places.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


def rotate(head):
    current = head
    prev = None
    while current.next:
        prev = current
        current = current.next
    if prev:
        prev.next = None

    current.next = head
    return current


def rotateList(head, k):
    if not head or not head.next:
        return head
    newHead = head
    current = head
    length = 0
    while current:
        length += 1
        current = current.next
    # print(length)  
    runs = k % length
    while runs:
        newHead = rotate(newHead)
        runs -= 1
        # print(k)s
    return newHead


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(0)
    llist.head.next = Node(1)
    llist.head.next.next = Node(2)
    # llist.head.next.next.next = Node(4)
    # llist.head.next.next.next.next = Node(5)
    # llist.printLL()
    llist.head = rotateList(llist.head, 1)
    llist.printLL()
