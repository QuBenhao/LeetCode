import {TreeNode,JSONArrayToTreeNode, TreeNodeToJSONArray} from "../../typescript/models/treenode";

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

/**
 Do not return anything, modify root in-place instead.
 */
function flatten(root: TreeNode | null): void {
	if (root === null) {
		return;
	}
	let left: TreeNode | null = root.left;
	let right: TreeNode | null = root.right;
	root.left = null;
	root.right = left;
	let p: TreeNode | null = root;
	while (p.right !== null) {
		p = p.right;
	}
	p.right = right;
	flatten(root.right);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	flatten(root)
	return TreeNodeToJSONArray(root);
}
