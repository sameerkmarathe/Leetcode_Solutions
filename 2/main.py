###################################################
############	2.Add Two Numbers	###########
###################################################

'''
There are two main approaches for this problem:
1. Iterative approach based on simple math framework
2. Recursive framework based as the same work is done per iteration call
'''

'''
We can solve this problem using simple rules for arithmetic addition
Create a new linked list to hold the sum of two numbers

Time Complexity: \Theta(max(length of linked lists)) as we iterate the maximum length among the linked lists exactly once.

Space Complexity: \Theta(max(length of linked list)) as the length of the answer will be at most one node more than the maximum of two linked lists' length. Note that we can mutate one of the linked list to store the answer but this will require us to find out the bigger linked list beforehand. Doing this optimization will offer smaller space complexity. 
'''

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


ans, carry = ListNode(), 0
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

'''
The second approach is recursion. This approach boasts almost same time complexity as the previous approach but uses constant memory due to its recursive nature.
Time Complexity: O(min(length of linked list)) as we stop recusing when we reach the end of the smaller list
Space Complexity: O(1) we do not maintain any data structure for the recusive approach.
'''

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
  
  if not l1: return l2
  if not l2: return l1
        
  val = l1.val + l2.val
  carry, val = divmod(val, 10)
        
  ans = ListNode(val)
  recurse = addTwoNumbers(l1.next, l2.next)
  
  ## Two different recursions based off the carry value
  ans.next = (addTwoNumbers(ListNode(carry), recurse), recurse)[carry == 0]
        
  return ans
