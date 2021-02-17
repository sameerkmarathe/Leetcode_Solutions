/**
*
*	19. Remove Nth node from the end of Linked List
*
**/

/*
Trick is to get the length of the list. But this is two iteration and slow.
A workaoround will be to get a slow and fast pointer, move the fast pointer ahead and let them meet. That point will be the node to be removed
Time Complexity:O(N) where N is the length of the list
Space Complexity: O(1) 
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode first = dummy;
    ListNode second = dummy;
    
    for (int i = 1; i <= n + 1; i++) {
        first = first.next;
    }
    
    while (first != null) {
        first = first.next;
        second = second.next;
    }
    second.next = second.next.next;
    return dummy.next;
}
}
