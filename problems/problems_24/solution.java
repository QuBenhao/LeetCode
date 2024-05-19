package problems.problems_24;

import qubhjava.models.ListNode;

/**
 * Definition for singly-linked list.
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head==null || head.next==null)
            return head;
        ListNode temp = head.next;
        head.next = swapPairs(temp.next);
        temp.next = head;
        return temp;
    }
}
