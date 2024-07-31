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

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
	if (root == null || root === p || root === q) {
        return root;
    }
    const left: TreeNode | null = lowestCommonAncestor(root.left, p, q);
    const right: TreeNode | null = lowestCommonAncestor(root.right, p, q);
    if (left != null && right != null) {
        return root;
    }
    return left != null ? left : right;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const targetVal1: number = JSON.parse(inputValues[1]);
	const targetVal2: number = JSON.parse(inputValues[2]);
	const nodes: Array<TreeNode | null> = JsonArrayToTreeNodeWithTargets(JSON.parse(inputValues[0]), targetVal1, targetVal2);
	const root: TreeNode = nodes[0], p: TreeNode = nodes[1], q: TreeNode = nodes[2];
	return TreeNodeToJSONArray(lowestCommonAncestor(root, p, q));
}