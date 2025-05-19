package problems.problems_LCR_028;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/


public class Solution extends BaseSolution {
    public Node flatten(Node head) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        Node head = FIXME(inputJsonValues[0])
        return JSON.toJSON(flatten(head));
    }
}
