package problems.problems_LCR_055;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
import qubhjava.models.TreeNode;


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class BSTIterator {

    public BSTIterator(TreeNode root) {

    }
    
    public int next() {

    }
    
    public boolean hasNext() {

    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		TreeNode root = TreeNode.ArrayToTreeNode(opValues[0][0]);
		BSTIterator obj = new BSTIterator(root);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("next") == 0) {
				
				ans.add(obj.next());
				continue;
			}
			if (operators[i].compareTo("hasNext") == 0) {
				
				ans.add(obj.hasNext());
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
