package problems.problems_LCR_043;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
import qubhjava.models.TreeNode;
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
class CBTInserter {

    public CBTInserter(TreeNode root) {

    }
    
    public int insert(int v) {

    }
    
    public TreeNode get_root() {

    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(v);
 * TreeNode param_2 = obj.get_root();
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		TreeNode root = TreeNode.ArrayToTreeNode(opValues[0][0]);
		CBTInserter obj = new CBTInserter(root);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("insert") == 0) {
				int v = Integer.parseInt(opValues[i][0]);
				ans.add(obj.insert(v));
				continue;
			}
			if (operators[i].compareTo("get_root") == 0) {
				
				ans.add(obj.TreeNode.TreeNodeToArray(get_root()));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
