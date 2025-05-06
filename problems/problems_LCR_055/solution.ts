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

class BSTIterator {
    constructor(root: TreeNode | null) {

    }

    next(): number {

    }

    hasNext(): boolean {

    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = new BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: BSTIterator = new BSTIterator(JSONArrayToTreeNode(opValues[0][0]));
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "next") {
			ans.push(obj.next());
			continue;
		}
		if (operators[i] == "hasNext") {
			ans.push(obj.hasNext());
			continue;
		}
		ans.push(null);
	}
	return ans;
}
