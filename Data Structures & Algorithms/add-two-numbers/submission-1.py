# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #non-empty linked lists
        #the second number or first number will always exist
        #non-negative integers
        #digits stored in reverse order, helps us with carrying
        #each digit create a separate node
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            value = num1 + num2 + carry
            carry = value // 10
            value = value % 10
            curr.next = ListNode(value)
            
            #update pointers
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
            