package problems.problems_445;

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
    private ListNode reverseList(ListNode node) {
        if (node == null || node.next == null) {
            return node;
        }
        ListNode newHead = reverseList(node.next);
        node.next.next = node;
        node.next = null;
        return newHead;
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l1r = reverseList(l1), l2r = reverseList(l2);
        ListNode dummy = new ListNode(), node = dummy;
        for (int cur = 0; l1r != null || l2r != null || cur > 0; node = node.next, cur /= 10) {
            if (l1r != null) {
                cur += l1r.val;
                l1r = l1r.next;
            }
            if (l2r != null) {
                cur += l2r.val;
                l2r = l2r.next;
            }
            node.next = new ListNode(cur % 10);
        }
        return reverseList(dummy.next);
    }

    @Override
    public Object solve(String[] values) {
        ListNode l1 = jsonArrayToListNode(values[0]);
		ListNode l2 = jsonArrayToListNode(values[1]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(addTwoNumbers(l1, l2)));
    }
}
