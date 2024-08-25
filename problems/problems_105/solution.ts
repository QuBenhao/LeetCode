import {TreeNode,TreeNodeToJSONArray} from "../../typescript/models/treenode";

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

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
	if (preorder.length == 0) {
		return null;
	}
	const root: TreeNode = new TreeNode(preorder[0]);
	const rootIndex: number = inorder.indexOf(preorder[0]);
	root.left = buildTree(preorder.slice(1, rootIndex + 1), inorder.slice(0, rootIndex));
	root.right = buildTree(preorder.slice(rootIndex + 1), inorder.slice(rootIndex + 1));
	return root;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const preorder: number[] = JSON.parse(inputValues[0]);
	const inorder: number[] = JSON.parse(inputValues[1]);
	return TreeNodeToJSONArray(buildTree(preorder, inorder));
}
