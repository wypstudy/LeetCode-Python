class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: [ListNode]):
        nums = []
        for node in lists:
            while node is not None:
                nums.append(node.val)
                node = node.next
        nums.sort()
        # 链表处理
        answer = ListNode(0)
        now = answer

        for num in nums:
            new_temp = ListNode(num)
            now.next = new_temp
            now = now.next
        return answer.next


instance = Solution()
