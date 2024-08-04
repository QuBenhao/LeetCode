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

function isValidBST(root: TreeNode | null): boolean {
    const dfs: Function = (node: TreeNode | null, lower: number, upper: number): boolean => {
		if (node === null) {
			return true;
		}
		if (node.val <= lower || node.val >= upper) {
			return false;
		}
		return dfs(node.left, lower, node.val) && dfs(node.right, node.val, upper);
	}
	return dfs(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	return isValidBST(root);
}
