# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not h or not h.next: return h
        t,n=h,1
        while t.next:t=t.next;n+=1
        k%=n
        if not k:return h
        t.next=h
        for _ in range(n-k):t=t.next
        h=t.next
        t.next=None
        return h