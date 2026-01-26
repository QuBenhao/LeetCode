function minCost(n: number, edges: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	return minCost(n, edges);
}
