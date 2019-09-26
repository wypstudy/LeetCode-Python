class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: [ListNode]):
        ## 链表处理
        answer = ListNode(0)
        now_node = answer
        length = len(lists)
        while True:
            next_queue = -1
            min_value = None
            for i in range(length):
                if lists[i] is not None:
                    if min_value is None or lists[i].val < min_value:
                        next_queue = i
                        min_value = lists[i].val
            if next_queue != -1:
                next_node = ListNode(min_value)
                now_node.next = next_node
                now_node = now_node.next
                lists[next_queue] = lists[next_queue].next
            else:
                break
        return answer.next


instance = Solution()
