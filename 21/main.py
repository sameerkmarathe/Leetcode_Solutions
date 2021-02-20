#######################################################
#####	21. Merge two sorted linked lists	#######
#######################################################


'''
The approach is the same. create a new list and apply the same merge logic from merge sort
Time Complexity:O(n+m) where n and m are the length of lists
Space Complexity:O(m+n) as we create a new list containing all the elements from input
'''

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
