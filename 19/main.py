#############################################################
#############	19.Remove Nth node from end of List	#####
#############################################################


'''
Trick is to get the length of the list. But this is two iteration and slow.
A workaoround will be to get a slow and fast pointer, move the fast pointer ahead and let them meet. That point will be the node to be removed
Time Complexity:O(N) where N is the length of the list
Space Complexity: O(1) 
'''

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
