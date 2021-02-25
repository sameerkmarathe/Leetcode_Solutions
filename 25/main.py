################################################
#######	25. Reverse Nodes in K-group	########
################################################


'''
Use a dummy head and when you reach k nodes reverse the linked lists
Time Complexity:O(n) As we only iterate a node once
Space Complexity:O(1) only constant references
'''

class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = left = right = head

        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1
            if count == k: 
                pre, cur = right, left
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, left = pre, left, right
            else:
                return dummy.next
