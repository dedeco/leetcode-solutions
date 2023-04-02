from typing import Optional

from basic.helpers import create_linked_list
from basic.link_list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None
        i = 0
        idx = {}
        prehead = ListNode(-999)
        prehead.next = head
        current = prehead
        while current:
            idx[i] = current
            if current.next:
                current = current.next
            else:
                break
            i += 1
        items = list(idx.keys())
        j = 0
        while items:
            cur = items.pop()
            if cur == 0:
                return prehead.next.next
            if j == n:
                temp = idx[cur]
                if temp.next and temp.next.next:
                    temp.next = temp.next.next
                else:
                    temp.next = None
                return prehead.next
            j += 1
        return prehead.next


if __name__ == "__main__":
    a = create_linked_list([1, 2, 4])

    current = Solution().removeNthFromEnd(a, 1)
    while current:
        print(current.val)
        current = current.next
