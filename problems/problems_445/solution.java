package problems.problems_445;

import qubhjava.models.ListNode;

import java.util.ArrayList;
import java.util.Collections;

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode c1 = l1, c2 = l2;
        ArrayList<Integer> n1 = new ArrayList<>(), n2 = new ArrayList<>();
        while (c1 != null) {
            n1.add(c1.val);
            c1 = c1.next;
        }
        while (c2 != null) {
            n2.add(c2.val);
            c2 = c2.next;
        }
        Collections.reverse(n1);
        Collections.reverse(n2);
        int carry = 0;
        ListNode curr = null, last = null;
        for (int i = 0; i < Math.max(n1.size(), n2.size()); i++) {
            int temp = 0;
            if ((i < n1.size() && n1.size() <= n2.size()) || (i < n2.size() && n2.size() < n1.size()))
                temp = n1.get(i) + n2.get(i) + carry;
            else if (n1.size() <= i)
                temp = n2.get(i) + carry;
            else
                temp = n1.get(i) + carry;
            if (temp >= 10) {
                temp -= 10;
                carry = 1;
            } else
                carry = 0;
            curr = new ListNode(temp, last);
            last = curr;
        }
        if (carry > 0)
            curr = new ListNode(carry, last);
        return curr;
    }
}
