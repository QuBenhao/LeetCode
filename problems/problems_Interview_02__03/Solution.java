package problems.problems_Interview_02__03;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class Solution extends BaseSolution {
    public void deleteNode(ListNode node) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
		int pos = Integer.parseInt(inputJsonValues[1]);
		ListNode head = ListNode.IntArrayToLinkedListCycle(arr, pos);
		deleteNode(node);
        return JSON.toJSON(ListNode.LinkedListToIntArray(node));
    }
}
