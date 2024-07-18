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

    public static int[] LinkedListToIntArray(ListNode node) {
        List<Integer> ans = new ArrayList<>();
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

    public static ListNode IntArrayToLinkedListCycle(int[] arr, int pos) {
        ListNode dummy = new ListNode();
        ListNode node = dummy;
        ListNode cycle = null;
        for (int i = 0; i < arr.length; i++) {
            node.next = new ListNode(arr[i]);
            node = node.next;
            if (i == pos) {
                cycle = node;
            }
        }
        node.next = cycle;
        return dummy.next;
    }

    public static ListNode[] IntArrayToIntersectionListNode(int[] arr1, int[] arr2, int iv, int idx1, int idx2) {
        ListNode headA = IntArrayToLinkedList(arr1);
        if (iv == 0 || idx1 == arr1.length || idx2 == arr2.length) {
            return new ListNode[]{headA, IntArrayToLinkedList(arr2)};
        }
        ListNode pa = headA;
        for (int i = 0; i < idx1; i++) {
            pa = pa.next;
        }
        ListNode headB = idx2 == 0 ? pa : new ListNode(arr2[0]);
        ListNode pb = headB;
        for (int i = 1; i < arr2.length - 1; i++) {
            pb.next = new ListNode(arr2[i]);
            pb = pb.next;
        }
        pb.next = pa;
        return new ListNode[]{headA, headB};
    }

}
