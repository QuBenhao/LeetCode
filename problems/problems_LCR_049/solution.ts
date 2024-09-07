import {JSONArrayToTreeNode, TreeNode} from "../../typescript/models/treenode";

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

function sumNumbers(root: TreeNode | null): number {
    let ans: number = 0;
    const dfs = (node: TreeNode | null, sum: number): void => {
        if (node === null) {
            return;
        }
        sum = sum * 10 + node.val;
        if (node.left === null && node.right === null) {
            ans += sum;
            return;
        }
        dfs(node.left, sum);
        dfs(node.right, sum);
    };
    dfs(root, 0);
    return ans;
};

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(inputValues[0]));
    return sumNumbers(root);
}
