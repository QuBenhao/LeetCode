function shortestPath(n: number, edges: number[][], labels: string, k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	const labels: string = JSON.parse(inputValues[2]);
	const k: number = JSON.parse(inputValues[3]);
	return shortestPath(n, edges, labels, k);
}
