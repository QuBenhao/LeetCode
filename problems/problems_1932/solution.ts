import {JSONArrayToTreeNodeArray,TreeNode,TreeNodeToJSONArray} from "../../typescript/models/treenode";

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

function canMerge(trees: Array<TreeNode | null>): TreeNode | null {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const trees: Array<TreeNode | null> = JSONArrayToTreeNodeArray(JSON.parse(inputValues[0]));
	return TreeNodeToJSONArray(canMerge(trees));
}
