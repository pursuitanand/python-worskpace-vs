from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# build a list: 1 -> 2 -> 3
l1 = ListNode(1, ListNode(2, ListNode(3)))

# iterate
curr = l1
while curr:
    #print(curr.val)
    #print(89 // 10)
    curr = curr.next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

s = Solution()
result = s.addTwoNumbers(l1, l2)

# Print the result
curr = result
while curr:
    print(curr.val)
    curr = curr.next