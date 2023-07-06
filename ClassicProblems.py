'''
This script is meant to take on various classic LinkedList problems
'''

def reverseLL(head):
    prev = None
    while head != None:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def removeElements(head, val):
    dummy = ListNode(next = head)
    prev = dummy
    while head != None:
        if head.val == val:
            prev.next = head.next
        else:
            prev = head
        head = head.next
    return dummy.next


def oddEven(head):
    pass


def isPalindromeBruteForce(head):
    lst = []
    while head != None:
        lst.append(head.val)
        head = head.next

    left = 0
    right = len(lst) - 1
    while left <= right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True
# Time complexity is O(n) but memory is O(n)


def isPalindromeOptimeal(head):
    slow = head
    fast = head
    # Find the middle of the linkedlist
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    # reverse the linkedlist
    prev = None
    while slow != None:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    # check palindrome, similar to an array
    left = head
    right = prev
    while right != None:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True