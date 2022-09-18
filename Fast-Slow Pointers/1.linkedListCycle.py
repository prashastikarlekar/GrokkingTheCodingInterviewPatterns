# https://leetcode.com/problems/linked-list-cycle/

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, 
# pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
 
class LinkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        current=self.head
        while current:
            print(current.value)
            current=current.next
    
# Floyd's cycle finding algorithm
def findCycleI(head):
    if not head: return False
    slow=head
    fast=head
    while(slow!=fast):
        if fast==None or fast.next==None: # there is no cycle as we reached end of the list
            return False
        slow=slow.next
        fast=fast.next.next
    return True

# Using Set
def findCycleII(head): 
    if not head: return False
    visitedNodes= set()
    current=head
    while current:
        if current in visitedNodes:
            return True
        visitedNodes.add(current)
        current=current.next
    return False

if __name__=="__main__":
    llist= LinkedList()
    llist.head=Node(3)
    llist.head.next=Node(0)
    llist.head.next.next=Node(2)
    llist.head.next.next.next=Node(4)
    llist.head.next.next.next.next=llist.head.next
    # llist.printList()
    print(findCycleI(llist.head))
    print(findCycleII(llist.head))


        
        