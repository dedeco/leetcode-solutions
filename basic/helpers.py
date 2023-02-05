from typing import List, Optional


def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    list1 = current = None
    for i in arr:
        if not list1:
            current = ListNode(i)
            list1 = current
        else:
            current.next = ListNode(i)
            current = current.next
    return list1
