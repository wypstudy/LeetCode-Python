# coding=utf-8
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = ListNode(0)
        now = first
        while l1 is not None or l2 is not None:
            # 加法和进位
            a = 0 if l1 is None else l1.val
            b = 0 if l2 is None else l2.val
            val = a + b + now.val
            value = val % 10
            carry = val / 10

            # 存储到链表
            now.val = value
            next_digit = ListNode(carry)

            # 进入下一位
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is not None or l2 is not None or next_digit.val > 0:
                now.next = next_digit
            now = next_digit
        return first


ins = Solution()
l1a = ListNode(2)
l1b = ListNode(4)
l1c = ListNode(3)
l2a = ListNode(5)
l2b = ListNode(6)
l2c = ListNode(4)
l1a.next = l1b
l1b.next = l1c
l2a.next = l2b
l2b.next = l2c
echo = ins.addTwoNumbers(l1a, l2a)
while True:
    if echo is None:
        break
    print echo.val
    echo = echo.next


