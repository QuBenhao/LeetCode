package problems.problems_2181;

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
    public ListNode mergeNodes(ListNode head) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy, node = head.next;
        while (node != null) {
            int s = 0;
            while (node != null && node.val != 0) {
                s += node.val;
                node = node.next;
            }
            cur.next = new ListNode(s);
            cur = cur.next;
            if (node != null) {
                node = node.next;
            }
        }
        return dummy.next;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode head = jsonArrayToListNode(inputJsonValues[0]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(mergeNodes(head)));
    }
}
