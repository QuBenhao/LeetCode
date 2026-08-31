package problems.problems_2058;

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
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        // 最小距离来自相邻临界点，最大距离来自首尾临界点
        int first = 0, prev = 0, mn = Integer.MAX_VALUE;
        ListNode a = head, b = head.next, c = head.next.next;
        for (int i = 2; c != null; ++i) {
            if (b.val > a.val && b.val > c.val || b.val < a.val && b.val < c.val) {
                if (prev > 0) mn = Math.min(mn, i - prev);
                else first = i;
                prev = i;
            }
            a = b; b = c; c = c.next;
        }
        return mn == Integer.MAX_VALUE ? new int[]{-1, -1} : new int[]{mn, prev - first};
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode head = jsonArrayToListNode(inputJsonValues[0]);
        return JSON.toJSON(nodesBetweenCriticalPoints(head));
    }
}
