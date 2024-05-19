package problems.problems_82;

import qubhjava.models.ListNode;

public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null)
            return null;
        int val = head.val;
        if (head.next != null && head.next.val == val) {
            while (head != null && head.val == val)
                head = head.next;
            return deleteDuplicates(head);
        } else {
            head.next = deleteDuplicates(head.next);
            return head;
        }
    }
}
