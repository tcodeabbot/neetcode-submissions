# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        result = []
        curr = head

        while curr:
            nodes.append(curr.val)
            curr = curr.next
        length = len(nodes)
        nodes.pop(length - n)

        dummy = ListNode()

        curr = dummy
        for i in range(len(nodes)):
            curr.next = ListNode(nodes[i])
            curr = curr.next

        return dummy.next