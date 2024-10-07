import {JSONArrayToTreeNode,TreeNodeToJSONArray,TreeNode} from "../../typescript/models/treenode";

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

function increasingBST(root: TreeNode | null): TreeNode | null {
	const dummy = new TreeNode();
	let current = dummy;
	
	const inorder = (node: TreeNode | null) => {
		if (!node) {
			return;
		}
		inorder(node.left);
		current.right = new TreeNode(node.val);
		current = current.right;
		inorder(node.right);
	};
	
	inorder(root);
	return dummy.right;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	return TreeNodeToJSONArray(increasingBST(root));
}
