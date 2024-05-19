package problems.problems_141;

import qubhjava.models.ListNode;

public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        while(fast != null){
            head = head.next;
            if(fast.next != null)
                fast = fast.next.next;
            else
                return false;
            if(fast == head)
                return true;
        }
        return false;
    }
}
