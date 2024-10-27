import {TreeNodeToJSONArray,TreeNode,JsonArrayToTreeNodeWithTargets} from "../../typescript/models/treenode";

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

function inorderSuccessor(root: TreeNode | null, p: TreeNode | null): TreeNode | null {
	if (root === null) {
		return null;
	}
	if (root.val <= p.val) {
		return inorderSuccessor(root.right, p);
	}
	const left: TreeNode | null = inorderSuccessor(root.left, p);
	return left === null ? root : left;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const targetVal1: number = JSON.parse(inputValues[1]);
	const nodes: Array<TreeNode | null> = JsonArrayToTreeNodeWithTargets(JSON.parse(inputValues[0]), targetVal1);
	const root: TreeNode = nodes[0], p: TreeNode = nodes[1];
	return TreeNodeToJSONArray(inorderSuccessor(root, p));
}
