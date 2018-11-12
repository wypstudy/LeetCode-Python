# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 0
        count_size_head = head
        while count_size_head is not None:
            size += 1
            count_size_head = count_size_head.next
        num = size - n + 1

        pre = None
        will_del = head
        while num > 1:
            num -= 1
            pre = will_del
            will_del = will_del.next
        if pre is None:
            head = head.next
        else:
            pre.next = will_del.next
        del will_del
        return head


instance = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
now = a
print("start")
while now is not None:
    print(now.val)
    now = now.next
now = instance.removeNthFromEnd(a, 2)
print("start")
while now is not None:
    print(now.val)
    now = now.next

