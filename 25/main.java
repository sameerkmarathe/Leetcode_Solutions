/**
*
*	25. Reverse Nodes in k-group
*
**/


/*
The approach is similar to the python one. Refer to the main.py code for further details
*/

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
    ListNode curr = head;
    int count = 0;
    while (curr != null && count != k) { 
        curr = curr.next;
        count++;
    }
    if (count == k) { 
        curr = reverseKGroup(curr, k); 
        
        while (count-- > 0) {  
            ListNode temp = head.next; 
            head.next = curr; 
            curr = head; 
            head = temp; 
        }
        head = curr;
    }
    return head;
}

}
