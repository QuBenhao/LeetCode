import {TreeNode,JSONArrayToTreeNode,TreeNodeToJSONArray} from "../../typescript/models/treenode";

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

/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
	if (root === null) {
		return "";
	}
	const result: Array<string> = [];
	const dfs = (node: TreeNode | null) => {
		if (node === null) {
			result.push("#");
			return;
		}
		result.push(node.val.toString());
		dfs(node.left);
		dfs(node.right);
	}
	dfs(root);
	while (result.length > 0 && result[result.length-1] === "#") {
		result.pop();
	}
	return result.join(",")
};

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
	if (data.length === 0) {
		return null;
	}
	const arr = data.split(",")
	let idx: number = 0;
	const dfs = () => {
		if (idx >= arr.length || arr[idx] === "#") {
			idx++;
			return null;
		}
		const node = new TreeNode(Number.parseInt(arr[idx++]));
		node.left = dfs();
		node.right = dfs();
		return node;
	}
	return dfs();
};


/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
	const s = serialize(root);
	return TreeNodeToJSONArray(deserialize(s));
}
