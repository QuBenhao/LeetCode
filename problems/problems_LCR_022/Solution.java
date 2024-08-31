package problems.problems_LCR_022;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for singly-linked list.
 * class ListNode {
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
    public ListNode detectCycle(ListNode head) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
		int pos = Integer.parseInt(inputJsonValues[1]);
		ListNode head = ListNode.IntArrayToLinkedListCycle(arr, pos);
        return JSON.toJSON(ListNode.LinkedListToIntArray(detectCycle(head)));
    }
}
