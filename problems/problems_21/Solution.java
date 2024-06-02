package problems.problems_21;

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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        for (ListNode node = dummy; list1 != null || list2 != null; node = node.next) {
            if (list2 != null && (list1 == null || list1.val > list2.val)) {
                node.next = new ListNode(list2.val);
                list2 = list2.next;
            } else {
                node.next = new ListNode(list1.val);
                list1 = list1.next;
            }
        }
        return dummy.next;
    }

    @Override
    public Object solve(String[] values) {
        ListNode list1 = jsonArrayToListNode(values[0]);
		ListNode list2 = jsonArrayToListNode(values[1]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(mergeTwoLists(list1, list2)));
    }
}
