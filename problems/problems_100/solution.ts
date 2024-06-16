import {TreeNode, JSONArrayToTreeNode} from "../../typescript/models/treenode";

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    return (p == null && q == null) || (p != null && q != null && p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right))
};

export function Solve(inputJsonElement: string): any {
    const splits: string[] = inputJsonElement.split("\n");
    const p: TreeNode | null = JSONArrayToTreeNode(JSON.parse(splits[0]));
    const q: TreeNode | null = JSONArrayToTreeNode(JSON.parse(splits[1]));
    return isSameTree(p, q)
}