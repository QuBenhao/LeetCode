import {JSONArrayToTreeNode,TreeNode} from "../../typescript/models/treenode";

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function minDepth(root: TreeNode | null): number {
	if (root == null) {
		return 0;
	}
	if (root.left == null && root.right == null) {
		return 1;
	}
	let ans: number = 0x3f3f3f;
	if (root.left != null) {
		ans = Math.min(ans, minDepth(root.left) + 1);
	}
	if (root.right != null) {
		ans = Math.min(ans, minDepth(root.right) + 1);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(splits[0]));
	return minDepth(root);
}
