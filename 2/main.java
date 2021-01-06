/*
		2. Add Two Numbers
*/

/*
More information about the approach can be found in main.py
*/

ListNode answer = new ListNode(0), curr = answer;
int carry = 0;
while (l1 != null || l2 != null) {

    int sum = carry;
    sum += (l1 == null) ? 0 : l1.val;
    sum += (l2 == null) ? 0 : l2.val;
    carry = sum / 10;
    curr.next = new ListNode(sum % 10);
    curr = curr.next;
    if (l1 != null) l1 = l1.next;
    if (l2 != null) l2 = l2.next;
}

curr.next = (carry > 0) ? new ListNode(carry) : null;

return answer.next;


