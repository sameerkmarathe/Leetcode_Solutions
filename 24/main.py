####################################################
########	24. Swap Nodes in Pairs	############
####################################################



'''
This problem can be recursively solved. Go recursively down to the end and build bottom up while keeping tab on every second node
Time Complexity:O(n) every node is visited once
Space Complexity:O(1) As we keep constant tabs`
'''

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second
