import {TreeNode,JSONArrayToTreeNode} from "../../typescript/models/treenode";

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

function maxPathSum(root: TreeNode | null): number {
	let ans: number = Number.MIN_SAFE_INTEGER;
	const dfs = (node: TreeNode | null): number => {
		if (node == null) {
			return 0;
		}
		const left: number = dfs(node.left);
		const right: number = dfs(node.right);
		ans = Math.max(ans, node.val + left + right);
		return Math.max(0, node.val + Math.max(left, right));
	}
	dfs(root);
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	return maxPathSum(root);
}
