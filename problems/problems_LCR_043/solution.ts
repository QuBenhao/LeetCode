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

class CBTInserter {
    private root: TreeNode | null = null;
    private n: number;

    constructor(root: TreeNode | null) {
        this.root = root;
        let n: number = 0;
        const dfs = (node: TreeNode | null): void => {
            if (node == null) {
                return;
            }
            n++;
            dfs(node.left);
            dfs(node.right);
        }
        dfs(root);
        this.n = n;
    }

    insert(v: number): number {
        this.n++;
		const highbit = ('' + this.n.toString(2)).length - 1;
        const child: TreeNode = new TreeNode(v);
        let node: TreeNode = this.root;
        for (let i: number = highbit - 1; i > 0; i--) {
            if ((this.n & (1 << i)) === 0) {
                node = node.left;
            } else {
                node = node.right;
            }
        }
		if ((this.n & 1) === 0) {
			node.left = child;
		} else {
			node.right = child;
		}
		return node.val;
    }

    get_root(): TreeNode | null {
        return this.root;
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
	const obj: CBTInserter = new CBTInserter(JSONArrayToTreeNode(opValues[0][0]));
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "insert") {
			ans.push(obj.insert(opValues[i][0]));
			continue;
		}
		if (operators[i] == "get_root") {
			ans.push(TreeNodeToJSONArray(obj.get_root()));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
