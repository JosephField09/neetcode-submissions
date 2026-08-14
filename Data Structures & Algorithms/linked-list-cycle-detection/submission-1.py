# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checked = set()
        node = head
        while node:
            if node in checked:
                return True
            else:
                checked.add(node)
                node = node.next
        return False