class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i, listVal in enumerate(lists):
            if listVal:
                heapq.heappush(arr, (listVal.val, i, listVal))
        temp = ListNode()
        current = temp
        while arr:
            val, i, node = heapq.heappop(arr)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(arr, (node.next.val, i, node.next))

        return temp.next
