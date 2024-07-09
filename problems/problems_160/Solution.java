package problems.problems_160;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
import qubhjava.models.ListNode;

public class Solution extends BaseSolution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pA = headA, pB = headB;
        while (pA != pB) {
            pA = pA == null ? headB : pA.next;
            pB = pB == null ? headA : pB.next;
        }
        return pA;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int iv = Integer.parseInt(inputJsonValues[0]);
        int[] arrA = jsonArrayToIntArray(inputJsonValues[1]);
		int[] arrB = jsonArrayToIntArray(inputJsonValues[2]);
        int idxA = Integer.parseInt(inputJsonValues[3]);
        int idxB = Integer.parseInt(inputJsonValues[4]);
        ListNode[] nodes = ListNode.IntArrayToIntersectionListNode(arrA, arrB, iv, idxA, idxB);
        ListNode headA = nodes[0], headB = nodes[1];
        ListNode result = getIntersectionNode(headA, headB);
        return JSON.toJSON(result != null ? result.val : null);
    }
}
