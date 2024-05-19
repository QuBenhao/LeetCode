class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null)
            return null;
        int val = head.val;
        if(head.next!=null && head.next.val == val){
            while(head!=null && head.val == val)
                head = head.next;
            return deleteDuplicates(head);
        }else{
            head.next = deleteDuplicates(head.next);
            return head;
        }
    }
}

/**
 * Definition for singly-linked list.
 */
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
