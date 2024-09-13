package problems.problems_LCR_043;

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
class CBTInserter {
	private final TreeNode root;
	private int n;

    public CBTInserter(TreeNode root) {
		this.root = root;
		int n = 0;
		Queue<TreeNode> q = new ArrayDeque<>();
		q.add(root);
		while (!q.isEmpty()) {
			TreeNode node = q.poll();
			n++;
			if (node.left != null) {
				q.add(node.left);
			}
			if (node.right != null) {
				q.add(node.right);
			}
		}
		this.n = n;
    }

    public int insert(int val) {
		n++;
		TreeNode node = root;
		int highbit = 31 - Integer.numberOfLeadingZeros(n);
		for (int i = highbit - 1; i > 0; i--) {
			if ((n & (1 << i)) == 0) {
				node = node.left;
			} else {
				node = node.right;
			}
		}
		if ((n & 1) == 0) {
			node.left = new TreeNode(val);
		} else {
			node.right = new TreeNode(val);
		}
		return node.val;
    }

    public TreeNode get_root() {
		return root;
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(val);
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
				int val = Integer.parseInt(opValues[i][0]);
				ans.add(obj.insert(val));
				continue;
			}
			if (operators[i].compareTo("get_root") == 0) {

				ans.add(TreeNode.TreeNodeToArray(obj.get_root()));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
