function edgeScore(edges: number[]): number {
	let ans: number = 0;
	const counter: number[] = new Array(edges.length).fill(0);
	for (const [i, edge] of edges.entries()) {
		counter[edge] += i;
		if (counter[edge] > counter[ans]) {
			ans = edge;
		} else if (counter[edge] === counter[ans] && edge < ans) {
			ans = edge;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const edges: number[] = JSON.parse(inputValues[0]);
	return edgeScore(edges);
}
