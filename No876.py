# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return

        s = []
        h = head
        while h is not None:
            s.append(h)
            h = h.next

        return s[len(s)/2]