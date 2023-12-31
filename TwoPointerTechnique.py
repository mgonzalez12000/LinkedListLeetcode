'''
Image there are two runner with different speeds. If they are running on
a striaght path, the fast runner will first arrive at the destination.
However, if they are running on a circular track, the fast runner
will catch up with the slow runner if they keep running.

Lets take a look at the Linked List cycle problem
'''

def cycle(head):
    '''
    - if there is no cycle, the fast pointer will stop at the end of the LL
    - If there is a cycle, the fast pointer will eventually meet with the slow pointer.
    '''
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def cycleII(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            '''
            - if there is a cycle, reset the slow pointer to the head
            - reset the slow pointer to head and then traverse both pointers by 1 step
            - The node where they meet is the starting index of the cycle.
            '''
            slow = head
            while slow != None and slow.next != None:
                slow = slow.next
                fast = fast.next
                if slow == fast:
                    slow = head
                    while slow != fast:
                        slow = slow.next
                        fast = fast.next
                    return slow
    return None


def intersection(headA, headB):
    '''
    return the node value when an intersection between both linkedlsits.
    '''
    hashSet = set()
    currA = headA
    currB = headB
    while currA != None:
        hashSet.add(currA)
        currA = currA.next
    while currB != None:
        if currB in hashSet:
            return currB
        currB = currB.next
    return None


# Remove node from nth of the end of the list
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def removeNthNode(head, n):
        '''
        Given the head of a linkedlist , remove the nth node from the end of
        the list and return its head
        '''
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        for i in range(n):
            right = right.next
        while right != None:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
    

'''
Here we provide a template to solve common two pointer problems using the
Linked list data structure

Assume you have a predefined ListNode method
'''

ListNode slow = head
ListNode fast = head
'''
Change this condition to satisfy certain problems. Can vary.
NOTICE: remember to avoid null point exceptions aka errors
'''
while slow != None and fast != None and fast.next = None:
    slow = slow.next # move slow pointer one step at a time
    fast = fast.next.next # move fast pointer two steps at a time
    if slow == fast: # change this condition to satisfy problem
        return True
return False # change rtype to satisfy problem

# Ignore errors, this is just an outline