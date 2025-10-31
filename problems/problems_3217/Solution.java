package problems.problems_3217;

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
    public ListNode modifiedList(int[] nums, ListNode head) {
        Set<Integer> s = new HashSet<>();
        for (int num: nums) {
            s.add(num);
        }
        ListNode dummy = new ListNode(-1, head);
        ListNode prev = dummy, curr = head;
        while (curr != null) {
            if (s.contains(curr.val)) {
                prev.next = curr.next;
            } else {
                prev = curr;
            }
            curr = curr.next;
        }
        return dummy.next;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		ListNode head = jsonArrayToListNode(inputJsonValues[1]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(modifiedList(nums, head)));
    }
}
