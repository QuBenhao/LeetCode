class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

function JSONArrayToTreeNode(jsonArray: any): TreeNode | null {
    return JsonArrayToTreeNodeWithTargets(jsonArray)[0];
}

function JsonArrayToTreeNodeWithTargets(jsonArray: any, ...targets: number[]): TreeNode[] {
    const ans: TreeNode[] = Array.from({length: targets.length + 1}, () => null);
    if (jsonArray == null || jsonArray.length === 0 || jsonArray[0] == null) {
        return ans;
    }
    const root: TreeNode | null = new TreeNode(jsonArray[0]);
    let isLeft: number = 1;
    const nodes: Array<TreeNode | null> = []
    let currNode: TreeNode | null = root;
    ans[0] = root;
    for (let i: number = 0; i < targets.length; i++) {
        if (root.val === targets[i]) {
            ans[i + 1] = root;
        }
    }
    for (let i = 1; i < jsonArray.length; i++) {
        let node: TreeNode | null = null;
        if (jsonArray[i] != null) {
            node = new TreeNode(jsonArray[i]);
            for (let i: number = 0; i < targets.length; i++) {
                if (node.val === targets[i]) {
                    ans[i + 1] = node;
                }
            }
        }
        if (isLeft == 1) {
            if (node != null) {
                // @ts-ignore
                currNode.left = node;
                nodes.push(node);
            }
        } else {
            if (node != null) {
                // @ts-ignore
                currNode.right = node;
                nodes.push(node);
            }
            currNode = nodes[0];
            nodes.shift();
        }
        isLeft ^= 1;
    }
    return ans;
}

function JSONArrayToTreeNodeArray(jsonArray: any): Array<TreeNode | null> {
    const ans: Array<TreeNode | null> = [];
    for (let i = 0; i < jsonArray.length; i++) {
        if (jsonArray[i] == null) {
            ans.push(null);
        } else {
            ans.push(JSONArrayToTreeNode(jsonArray[i]));
        }
    }
    return ans;
}

function TreeNodeToJSONArray(root: TreeNode | null): Array<number | null> {
    const ans: Array<number | null> = [];
    const list: Array<TreeNode | null> = [];
    list.push(root);
    for (let idx = 0; idx < list.length; idx++) {
        const node: TreeNode | null = list[idx];
        if (node == null) {
            ans.push(null);
        } else {
            ans.push(node.val);
            list.push(node.left);
            list.push(node.right);
        }
    }
    while (ans.length > 0 && ans[ans.length - 1] == null) {
        ans.pop();
    }
    return ans;
}

export {TreeNode, JSONArrayToTreeNode, TreeNodeToJSONArray, JSONArrayToTreeNodeArray};