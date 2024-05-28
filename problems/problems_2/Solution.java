package problems.problems_2;

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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode node = dummy;
        int addition = 0;
        while (l1 != null || l2 != null || addition != 0) {
            int cur = addition;
            if (l1 != null) {
                cur += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                cur += l2.val;
                l2 = l2.next;
            }
            node.next = new ListNode(cur % 10);
            node = node.next;
            addition = cur >= 10 ? 1 : 0;
        }
        return dummy.next;
    }

    @Override
    public Object solve(String[] values) {
        ListNode l1 = jsonArrayToListNode(values[0]);
		ListNode l2 = jsonArrayToListNode(values[1]);
        return JSON.toJSON(addTwoNumbers(l1, l2).LinkedListToIntArray());
    }
}
