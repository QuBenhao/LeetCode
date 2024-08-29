package problems.problems_LCR_048;

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
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("serialize") == 0) {
				TreeNode root = TreeNode.ArrayToTreeNode(opValues[i][0]);
				ans.add(obj.serialize(root));
				continue;
			}
			if (operators[i].compareTo("deserialize") == 0) {
				String data = jsonStringToString(opValues[i][0]);
				ans.add(obj.TreeNode.TreeNodeToArray(deserialize(data)));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
