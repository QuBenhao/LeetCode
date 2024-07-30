//Definition for _Node.
class NodeRandom {
    val: number
    next: NodeRandom | null
    random: NodeRandom | null

    constructor(val?: number, next?: NodeRandom, random?: NodeRandom) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
        this.random = (random === undefined ? null : random)
    }
}

function JSONArrayToNodeRandom(jsonArray: any): NodeRandom | null {
    if (jsonArray == null || jsonArray.length === 0 || jsonArray[0] == null) {
        return null;
    }
    const nodes: Array<NodeRandom | null> = new Array(jsonArray.length);
    let lastNode: NodeRandom | null = null;
    for (let i: number = jsonArray.length - 1; i >= 0; i--) {
        nodes[i] = new NodeRandom(jsonArray[i][0], lastNode);
        lastNode = nodes[i];
    }
    for (let i: number = 0; i < jsonArray.length; i++) {
        if (jsonArray[i][1] != null) {
            nodes[i].random = nodes[jsonArray[i][1]];
        }
    }
    return nodes[0];
}

function NodeRandomToJSONArray(root: NodeRandom | null): Array<Array<number | null>> {
    const result: Array<Array<number | null>> = [];
    if (root == null) {
        return result;
    }
    const idxMap: Map<NodeRandom, number> = new Map();
    let idx: number = 0;
    let head: NodeRandom | null = root;
    while (head != null) {
        idxMap.set(head, idx++);
        head = head.next;
    }
    head = root;
    while (head != null) {
        const cur: Array<number | null> = [head.val, head.random == null ? null : idxMap.get(head.random)];
        result.push(cur);
        head = head.next;
    }
    return result;
}

export { NodeRandom, JSONArrayToNodeRandom, NodeRandomToJSONArray};
