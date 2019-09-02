# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        tail = head
        while l1 is not None or l2 is not None:
            while (l1 is not None and l2 is not None and l1.val <= l2.val) or (l1 is not None and l2 is None):
                tail.next = ListNode(l1.val)
                tail = tail.next
                l1 = l1.next
            while (l1 is not None and l2 is not None and l2.val <= l1.val) or (l1 is None and l2 is not None):
                tail.next = ListNode(l2.val)
                tail = tail.next
                l2 = l2.next
        return head.next


instance = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b

c.next = d
d.next = e
now = a
print("start")
while now is not None:
    print(now.val)
    now = now.next
now = instance.mergeTwoLists(a, c)
print("start")
while now is not None:
    print(now.val)
    now = now.next
