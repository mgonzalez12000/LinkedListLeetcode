# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity is o(n)
class Solution(object):
    def isPalindrome(self, head):
        stack =[]
        isPalindrome = True
        dummy = head

        while dummy != None:
            stack.append(dummy.val)
            dummy = dummy.next
        
        while head != None and isPalindrome != False:
            curr = stack.pop()
            if curr == head.val:
                isPalindrome = True
            else:
                isPalindrome = False
            head = head.next
            
        return isPalindrome
    

# Second approach is worst time complexity using two pointer teq. o(n log(n))
class alternative(object):
    def isPalindrome(self, head):
        stack = []        
        left = 0
        right = len(stack) - 1
        while head != None:
            stack.append(head.val)
            head = head.next
        while left <= right:
            if stack[left] == stack[right]:
                left += 1
                right -= 1
            else:
                return False
        return True