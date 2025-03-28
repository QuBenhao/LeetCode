function longestCycle(edges: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const edges: number[] = JSON.parse(inputValues[0]);
	return longestCycle(edges);
}
