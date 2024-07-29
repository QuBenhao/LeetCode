//Definition for NodeNeighbors.
class NodeNeighbors {
    val: number
    neighbors: NodeNeighbors[]

    constructor(val?: number, neighbors?: NodeNeighbors[]) {
        this.val = (val===undefined ? 0 : val)
        this.neighbors = (neighbors===undefined ? [] : neighbors)
    }
}

function JsonArrayToNodeNeighbors(arr: Array<Array<number>>): NodeNeighbors | null {
    if (arr == null || arr.length === 0 || arr[0] == null) {
        return null;
    }
    const nodes: Array<NodeNeighbors | null> = new Array<NodeNeighbors | null>(arr.length + 1).fill(null);
    for (let i: number = 1; i < arr.length + 1; i++) {
        nodes[i] = new NodeNeighbors(i);
    }
    for (let i: number = 0; i < arr.length; i++) {
        const node: NodeNeighbors | null = nodes[i + 1];
        for (const neighbor of arr[i]) {
            node.neighbors.push(nodes[neighbor]);
        }
    }
    return nodes[1];
}

function NodeNeighborsToJsonArray(node: NodeNeighbors | null): Array<Array<number>> {
    const ans: Array<Array<number>> = [];
    if (node == null) {
        return ans;
    }
    const visited: Set<number> = new Set<number>();
    const dfs: Function = (node: NodeNeighbors | null): void => {
        for (let i: number = ans.length; i < node.val; i++) {
            ans.push([]);
        }
        for (const neighbor of node.neighbors) {
            ans[node.val - 1].push(neighbor.val);
            if (!visited.has(neighbor.val)) {
                visited.add(neighbor.val);
                dfs(neighbor);
            }
        }
    }
    visited.add(node.val);
    dfs(node);
    return ans;
}

export {NodeNeighbors, JsonArrayToNodeNeighbors, NodeNeighborsToJsonArray};