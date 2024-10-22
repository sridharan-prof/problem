# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = ''
        lst2 = ''
        while l1:
            lst1 += str(l1.val)
            l1 = l1.next

        while l2:
            lst2 += str(l2.val)
            l2 = l2.next
        ans = str(int(str(lst1[::-1])) + int(str(lst2[::-1]))) 
        print(ans)

        ll = ListNode(0)
        cur = ll

        prev = None
        for i in str(ans):
            node = ListNode(int(i))
            node.next = prev
            prev = node

        return prev
        
