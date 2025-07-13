package problems.problems_1290;

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
    public int getDecimalValue(ListNode head) {
        int ans = 0;
        for (ListNode node = head; node != null; node = node.next) {
            ans <<= 1;
            ans |= node.val;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode head = jsonArrayToListNode(inputJsonValues[0]);
        return JSON.toJSON(getDecimalValue(head));
    }
}
