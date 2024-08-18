package problems.problems_25;

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
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null) {
            return null;
        }
        ListNode node = head;
        for (int i = 0; i < k - 1; i++) {
            if (node == null) {
                return head;
            }
            node = node.next;
        }
        if (node == null) {
            return head;
        }
        node.next = reverseKGroup(node.next, k);
        ListNode tail = node.next, last = tail;
        while (head != last) {
            ListNode next = head.next;
            head.next = tail;
            tail = head;
            head = next;
        }
        return node;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode head = jsonArrayToListNode(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(reverseKGroup(head, k)));
    }
}
