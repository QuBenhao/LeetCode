package problems.problems_19;

import qubhjava.models.ListNode;

public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return null;
        ListNode front = head, back = head;
        for (int i = 0; i < n; i++)
            front = front.next;
        if (front == null) {
            return head.next;
        }
        while (front.next != null) {
            front = front.next;
            back = back.next;
        }
        back.next = back.next.next;
        return head;
    }
}
