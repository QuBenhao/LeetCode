class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode curr1 = l1;
        ListNode curr2 = l2;
        ListNode head = new ListNode();
        ListNode curr = head;
        int addone = 0;
        int num1 = 0;
        int num2 = 0;
        int sum = 0;
        while(curr1 != null || curr2!=null){
            if(curr1 == null)
                num1 = 0;
            else{
                num1 = curr1.val;
                curr1 = curr1.next;
            }
            if(curr2 == null)
                num2 = 0;
            else{
                num2 = curr2.val;
                curr2 = curr2.next;
            }
            sum = num1 + num2 + addone;
            if(sum>=10){
                addone = 1;
                curr.next = new ListNode(sum%10);
            }
            else{
                addone = 0;
                curr.next = new ListNode(sum);
            }
            curr = curr.next;
        }
        if(addone==1)
            curr.next = new ListNode(1);

        return head.next;
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
