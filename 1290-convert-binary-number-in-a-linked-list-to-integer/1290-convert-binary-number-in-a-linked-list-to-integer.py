# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary = [head.val]
        node = head
        while node.next is not None:
            node = node.next
            binary.append(node.val)

        out = 0
        for i in range(len(binary) - 1, - 1, -1):
            out += binary[i] * 2**(len(binary) - 1 - i)

        return out

        