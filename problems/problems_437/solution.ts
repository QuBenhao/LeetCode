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

function pathSum(root: TreeNode | null, targetSum: number): number {
    const dfs = (node: TreeNode | null, counter: Map<number, number>, sum: number): number => {
		if (node === null) {
			return 0;
		}
		let result: number = 0;
		sum += node.val;
		result += counter.get(sum - targetSum) || 0;
		counter.set(sum, (counter.get(sum) || 0) + 1);
		result += dfs(node.left, counter, sum);
		result += dfs(node.right, counter, sum);
		counter.set(sum, (counter.get(sum) || 0) - 1);
		return result;
	}
	return dfs(root, new Map<number, number>().set(0, 1), 0);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	const targetSum: number = JSON.parse(inputValues[1]);
	return pathSum(root, targetSum);
}
