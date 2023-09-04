# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def add(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)

            sum = l1.val + l2.val + carry 
            node = ListNode(sum%10)
            node.next = add(l1.next, l2.next, sum//10)
            return node

        return add(l1, l2, 0)
