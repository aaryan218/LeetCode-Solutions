# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        pre = dummy

        while True:
            node = pre
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next

            nxt = node.next    
            cur, prev = pre.next, nxt

            while cur != nxt:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            pre.next, pre = node, pre.next