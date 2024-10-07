function allPathsSourceTarget(graph: number[][]): number[][] {
	const result: number[][] = [];
	const dfs = (node: number, path: number[]) => {
		path.push(node);
		if (node === graph.length - 1) {
			result.push([...path]);
		} else {
			for (const neighbor of graph[node]) {
				dfs(neighbor, path);
			}
		}
		path.pop();
	};
	dfs(0, []);
	return result;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const graph: number[][] = JSON.parse(inputValues[0]);
	return allPathsSourceTarget(graph);
}
