#######################################################
############	23. Merge K sorted Lists	#######
#######################################################


'''
There is always a practical solution to such hard problems. Here we can just add all 
values of the linked lists to an array sort the array and populate a new linked list. This is memory intensive but incredibly simple
Time Complexity:O(log(nlogn)) n is the total length of all linked lists
Space Complexity: O(n)
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
