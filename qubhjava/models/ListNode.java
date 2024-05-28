package qubhjava.models;

import java.util.ArrayList;
import java.util.List;

public class ListNode {
    public int val;
    public ListNode next;

    public ListNode() {
    }

    public ListNode(int val) {
        this.val = val;
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public int[] LinkedListToIntArray() {
        List<Integer> ans = new ArrayList<>();
        ListNode node = this;
        while (node != null) {
            ans.add(node.val);
            node = node.next;
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }

    public static ListNode IntArrayToLinkedList(int[] arr) {
        ListNode dummy = new ListNode();
        ListNode node = dummy;
        for (int v: arr) {
            node.next = new ListNode(v);
            node = node.next;
        }
        return dummy.next;
    }

}
