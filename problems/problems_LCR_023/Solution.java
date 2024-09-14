package problems.problems_LCR_023;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;
import qubhjava.models.ListNode;

public class Solution extends BaseSolution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pA = headA, pB = headB;
        while (pA != pB) {
            pA = pA != null ? pA.next : headB;
            pB = pB != null ? pB.next : headA;
        }
        return pA;
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
