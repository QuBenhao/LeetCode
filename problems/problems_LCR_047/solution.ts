import {JSONArrayToTreeNode,TreeNode,TreeNodeToJSONArray} from "../../typescript/models/treenode";

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

function pruneTree(root: TreeNode | null): TreeNode | null {
	if (root === null) {
		return null;
	}
	root.left = pruneTree(root.left);
	root.right = pruneTree(root.right);
	if (root.left === null && root.right === null && root.val === 0) {
		return null;
	}
	return root;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	return TreeNodeToJSONArray(pruneTree(root));
}
