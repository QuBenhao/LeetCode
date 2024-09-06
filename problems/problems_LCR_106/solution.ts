function isBipartite(graph: number[][]): boolean {
	const n: number = graph.length;
	const color: number[] = new Array(n).fill(-1);
	const dfs = (node: number, c: number) => {
		if (color[node] !== -1) {
			return color[node] === c;
		}
		color[node] = c;
		const nxt: number = 1 ^ c;
		for (const other of graph[node]) {
			if (!dfs(other, nxt)) {
				return false;
			}
		}
		return true;
	}
	for (let i: number = 0; i < n; i++) {
		if (color[i] != -1) {
			continue;
		}
		if (!dfs(i, 0)) {
			return false;
		}
	}
	return true;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const graph: number[][] = JSON.parse(inputValues[0]);
	return isBipartite(graph);
}
