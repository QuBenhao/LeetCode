package problems.problems_2;

import qubhjava.models.ListNode;

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        ListNode curr = head;
        int addone = 0, num1 = 0, num2 = 0, sum = 0;
        while (l1 != null || l2 != null) {
            if (l1 == null)
                num1 = 0;
            else {
                num1 = l1.val;
                l1 = l1.next;
            }
            if (l2 == null)
                num2 = 0;
            else {
                num2 = l2.val;
                l2 = l2.next;
            }
            sum = num1 + num2 + addone;
            if (sum >= 10) {
                addone = 1;
                curr.next = new ListNode(sum % 10);
            } else {
                addone = 0;
                curr.next = new ListNode(sum);
            }
            curr = curr.next;
        }
        if (addone == 1)
            curr.next = new ListNode(1);

        return head.next;
    }
}
