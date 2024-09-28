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

function largestValues(root: TreeNode | null): number[] {
	if (!root) {
		return [];
	}
	const res: number[] = [];
	const queue: TreeNode[] = [root];
	while (queue.length > 0) {
		const size: number = queue.length;
		let max: number = -Infinity;
		for (let i: number = 0; i < size; i++) {
			const node: TreeNode = queue.shift();
			max = Math.max(max, node.val);
			if (node.left) {
				queue.push(node.left);
			}
			if (node.right) {
				queue.push(node.right);
			}
		}
		res.push(max);
	}
	return res;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	return largestValues(root);
}
