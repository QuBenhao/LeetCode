//Definition for NodeNext.
class NodeNext {
    val: number
    left: NodeNext | null
    right: NodeNext | null
    next: NodeNext | null

    constructor(val?: number, left?: NodeNext, right?: NodeNext, next?: NodeNext) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
        this.next = (next === undefined ? null : next)
    }
}

function JSONArrayToTreeNodeNext(jsonArray: any): NodeNext | null {
    if (jsonArray == null || jsonArray.length === 0 || jsonArray[0] == null) {
        return null;
    }
    const root: NodeNext | null = new NodeNext(jsonArray[0]);
    let isLeft: number = 1;
    const nodes: Array<NodeNext | null> = []
    let currNode: NodeNext | null = root;
    for (let i = 1; i < jsonArray.length; i++) {
        let node: NodeNext | null = null;
        if (jsonArray[i] != null) {
            node = new NodeNext(jsonArray[i]);
        }
        if (isLeft != 1) {
            if (node != null) {
                // @ts-ignore
                currNode.right = node;
                nodes.push(node);
            }
            currNode = nodes[0];
            nodes.shift();

        } else {
            if (node != null) {
                // @ts-ignore
                currNode.left = node;
                nodes.push(node);
            }
        }
        isLeft ^= 1;
    }
    return root;
}

function TreeNodeNextToJSONArray(root: NodeNext | null): Array<number | null> {
    const result: Array<number | null> = [];
    if (root == null) {
        return result;
    }
    let head: NodeNext | null = root;
    while (head != null) {
        let curr: NodeNext | null = head, nextHead: NodeNext | null = null;
        while (curr != null) {
            if (nextHead === null) {
                nextHead = curr.left === null ? curr.right : curr.left;
            }
            result.push(curr.val);
            curr = curr.next;
        }
        result.push(null);
        head = head.left;
    }
    return result;
}

export {NodeNext, JSONArrayToTreeNodeNext, TreeNodeNextToJSONArray};
