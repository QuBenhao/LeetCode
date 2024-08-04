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

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
	const dfs: Function = (node: TreeNode | null, subNode: TreeNode | null, mustMatch: boolean) => {
		if (node === null || subNode === null) {
			return node === subNode;
		}
		if (node.val === subNode.val && dfs(node.left, subNode.left, true) && dfs(node.right, subNode.right, true)) {
			return true;
		}
		if (mustMatch) {
			return false;
		}
		return dfs(node.left, subNode, false) || dfs(node.right, subNode, false);
	}
	return dfs(root, subRoot, false);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	const subRoot: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[1]));
	return isSubtree(root, subRoot);
}
