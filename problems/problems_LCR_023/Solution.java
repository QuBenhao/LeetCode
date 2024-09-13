package problems.problems_LCR_023;

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
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int iv = Integer.parseInt(inputJsonValues[0]);
		int[] arrA = jsonArrayToIntArray(inputJsonValues[1]);
		int[] arrB = jsonArrayToIntArray(inputJsonValues[2]);
		int skipA = Integer.parseInt(inputJsonValues[3]);
		int skipB = Integer.parseInt(inputJsonValues[4]);
		ListNode[] nodes = ListNode.IntArrayToIntersectionListNode(arrA, arrB, iv, skipA, skipB);
		ListNode headA = nodes[0], headB = nodes[1];
        return JSON.toJSON(ListNode.LinkedListToIntArray(getIntersectionNode(headA, headB)));
    }
}
