function maximumDetonation(bombs: number[][]): number {
	const n: number = bombs.length;
	const graph: number[][] = [];
	for (let i: number = 0; i < n; i++) {
		graph.push([]);
		const [x1, y1, r1] = bombs[i];
		for (let j: number = 0; j < n; j++) {
			const [x2, y2, r2] = bombs[j];
			const distance: number = (x1 - x2) ** 2 + (y1 - y2) ** 2;
			if (distance <= r1 * r1) {
				graph[i].push(j);
			}
		}
	}
	let ans: number = 0;
	const visited: boolean[] = new Array(n);

	for (let i: number = 0; i < n; i++) {
		visited.fill(false);
		let cur: number = 0;

		const dfs: Function = (u: number): void => {
			visited[u] = true;
			cur++;
			for (const v of graph[u]) {
				if (!visited[v]) {
					dfs(v);
				}
			}
		};
		dfs(i);
		ans = Math.max(ans, cur);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const bombs: number[][] = JSON.parse(inputValues[0]);
	return maximumDetonation(bombs);
}
