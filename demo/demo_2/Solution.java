package demo.demo_2;

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

    }

    @Override
    public Object solve(String[] values) {
        ListNode l1 = jsonArrayToListNode(values[0]);
		ListNode l2 = jsonArrayToListNode(values[1]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(addTwoNumbers(l1, l2)));
    }
}
