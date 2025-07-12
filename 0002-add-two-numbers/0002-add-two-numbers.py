# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        increment = 0
        sum_digit = l1.val + l2.val
        if sum_digit >= 10:
            result.append(sum_digit % 10)
            increment = 1
        else:
            result.append(sum_digit)
        while l1.next is not None and l2.next is not None:
            l1 = l1.next
            l2 = l2.next
            sum_digit = l1.val + l2.val
            if increment == 1:
                sum_digit += 1
                increment = 0
                
            if sum_digit >= 10:
                result.append(sum_digit%10)
                increment = 1
            else:
                result.append(sum_digit)


        while l1.next is not None:
            l1 = l1.next
            l1_val = l1.val
            if increment == 1:
                l1_val += 1
                increment = 0
                
            result.append(l1_val % 10)
            increment = l1_val // 10

        while l2.next is not None:
            l2 = l2.next
            l2_val = l2.val
            if increment == 1:
                l2_val += 1
                increment = 0
                
            result.append(l2_val % 10)
            increment = l2_val // 10

        if increment == 1:
            result.append(increment)
            

        print(result)
        node = ListNode(result[-1])
        for j in range(len(result) - 2, -1, -1):
            node = ListNode(val = result[j], next = node)

        return node
            

            