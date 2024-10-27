function find(parent: number[], i: number): number {
	if (parent[i] === i) {
		return i;
	}
	return find(parent, parent[i]);
}

function findRedundantConnection(edges: number[][]): number[] {
	const parent: number[] = new Array(edges.length + 1).fill(0);
	for (let i = 0; i < parent.length; i++) {
		parent[i] = i;
	}
	for (const edge of edges) {
		const x = find(parent, edge[0]);
		const y = find(parent, edge[1]);
		if (x === y) {
			return edge;
		}
		parent[x] = y;
	}
	return [0, 0];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const edges: number[][] = JSON.parse(inputValues[0]);
	return findRedundantConnection(edges);
}
