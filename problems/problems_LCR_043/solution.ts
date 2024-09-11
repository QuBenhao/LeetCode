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

class CBTInserter {
    constructor(root: TreeNode | null) {

    }

    insert(v: number): number {

    }

    get_root(): TreeNode | null {

    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * var obj = new CBTInserter(root)
 * var param_1 = obj.insert(v)
 * var param_2 = obj.get_root()
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: CBTInserter = new CBTInserter(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "insert") {
			ans.push(obj.insert(opValues[i][0]));
			continue;
		}
		if (operators[i] == "get_root") {
			ans.push(obj.get_root());
			continue;
		}
		ans.push(null);
	}
	return ans;
}
