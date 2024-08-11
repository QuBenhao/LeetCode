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

function kthSmallest(root: TreeNode | null, k: number): number {
    const ans: number[] = [];
	const inorder: Function = (node: TreeNode | null) => {
		if (!node) {
			return;
		}
		inorder(node.left);
		ans.push(node.val);
		inorder(node.right);
	}
	inorder(root);
	return ans[k - 1];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	const k: number = JSON.parse(inputValues[1]);
	return kthSmallest(root, k);
}
