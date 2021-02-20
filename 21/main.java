/**
*
*	13. Merge two sorted linked lists
*
**/


/*
We need to perform same logic as the merge logic of merge sort
Time Complexity:O(n) because we traverse each element of both lists once
Space Complexity:O(n) as we store each input element
*/

class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode prev= new ListNode(0);
        ListNode ans=prev;
        
            while(l1!=null || l2!=null){
                if (l1==null){
                    ListNode cur=new ListNode(l2.val);
                    prev.next=cur;
                    prev=cur;
                    l2=l2.next;
                }
                else if (l2==null){
                    ListNode cur=new ListNode(l1.val);
                    prev.next=cur;
                    prev=cur;
                    l1=l1.next; 
                }
                else if(l1.val<=l2.val){
                    ListNode cur=new ListNode(l1.val);
                    prev.next=cur;
                    prev=cur;
                    l1=l1.next; 
                    
                    
                }
                else{
                    ListNode cur=new ListNode(l2.val);
                    prev.next=cur;
                    prev=cur;
                    l2=l2.next; 

                }
                
                
            }
        return ans.next;
        
        
    }
}
