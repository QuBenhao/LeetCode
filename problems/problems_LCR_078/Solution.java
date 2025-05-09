package problems.problems_LCR_078;

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
    public ListNode mergeKLists(ListNode[] lists) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode[] lists = jsonArrayToListNodeArray(inputJsonValues[0]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(mergeKLists(lists)));
    }
}
