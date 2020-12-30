###################################################
############	2.Add Two Numbers	###########
###################################################

'''
We can solve this problem using simple rules for arithmetic addition
Create a new linked list to hold the sum of two numbers

Time Complexity: \Theta(max(length of linked lists)) as we iterate the maximum length among the linked lists exactly once.

Space Complexity: \Theta(max(length of linked list)) as the length of the answer will be at most one node more than the maximum of two linked lists' length. Note that we can mutate one of the linked list to store the answer but this will require us to find out the bigger linked list beforehand. Doing this optimization will offer smaller space complexity. 
'''
ans, carry = ListNode(0), 0
sumnode = ans
while l1 or l2:
  nodeval = carry
  if l1:
    nodeval += l1.val
  if l2:
    nodeval += l2.val
  carry, nodeval = divmod(nodeval, 10)
  sumnode.next = ListNode(nodeval)
  sumnode = sumnode.next
  l1 = l1.next if l1 else l1
  l2 = l2.next if l2 else l2
        
if carry:
  sumnode.next = ListNode(carry)

return ans.next
