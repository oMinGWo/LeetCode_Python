from models import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        x = 0
        h = None
        hh = None
        while True:
            a = 0 if l1 is None else l1.val
            b = 0 if l2 is None else l2.val
            y = (a + b + x) % 10
            x = (a + b + x) / 10
            ll = ListNode(y)
            if h is None:
                h = ll
                hh = ll
            else:
                h.next = ll
                h = ll
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is None and l2 is None and x == 0:
                return hh


if __name__ == '__main__':
    l1 = ListNode(5)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)

    l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    s = Solution()
    print s.addTwoNumbers(l1, l2).val
    print s.addTwoNumbers(l1, l2).next.val
    # print s.addTwoNumbers(l1, l2).next.next.val
