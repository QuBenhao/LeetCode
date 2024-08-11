package problems.problems_19;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
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
import qubhjava.models.ListNode;

public class Solution extends BaseSolution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) {
            return null;
        }
        ListNode slow = head, fast = head;
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }
        if (fast == null) {
            return head.next;
        }
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        return head;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode head = jsonArrayToListNode(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(removeNthFromEnd(head, n)));
    }
}
