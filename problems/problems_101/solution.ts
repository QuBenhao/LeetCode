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

function isSymmetric(root: TreeNode | null): boolean {
	const dfs: Function = (left: TreeNode | null, right: TreeNode | null): boolean => {
		if (left === null && right === null) {
			return true;
		}
		if (left === null || right === null || left.val !== right.val) {
			return false;
		}
		return dfs(left.left, right.right) && dfs(left.right, right.left);
	}
	return  root === null || dfs(root.left, root.right);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	return isSymmetric(root);
}
