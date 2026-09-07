# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        curr = head
        dummy = ListNode(0)
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        
        curr = dummy
        for i in range(len(nodes) - 1, -1, -1):
            curr.next = ListNode(nodes[i])
            curr = curr.next

        return dummy.next



            