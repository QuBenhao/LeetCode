function isBipartite(graph: number[][]): boolean {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const graph: number[][] = JSON.parse(inputValues[0]);
	return isBipartite(graph);
}
