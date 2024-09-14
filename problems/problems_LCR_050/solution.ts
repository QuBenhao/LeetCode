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

function pathSum(root: TreeNode | null, targetSum: number): number {
	const map: Map<number, number> = new Map();
	const dfs = (node: TreeNode | null, cur: number) => {
		if (node === null) {
			return 0;
		}
		cur += node.val;
		let ans: number = map.get(cur - targetSum) || 0;
		map.set(cur, (map.get(cur) || 0) + 1);
		ans += dfs(node.left, cur);
		ans += dfs(node.right, cur);
		map.set(cur, (map.get(cur) || 0) - 1);
		return ans;
	}
	map.set(0, 1);
	return dfs(root, 0);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	const targetSum: number = JSON.parse(inputValues[1]);
	return pathSum(root, targetSum);
}
