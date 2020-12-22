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

/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}
