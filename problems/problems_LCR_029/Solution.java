package problems.problems_LCR_029;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/


public class Solution extends BaseSolution {
    public Node insert(Node head, int insertVal) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        Node head = FIXME(inputJsonValues[0])
		int insertVal = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(insert(head, insertVal));
    }
}
