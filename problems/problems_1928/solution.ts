function minCost(maxTime: number, edges: number[][], passingFees: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const maxTime: number = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	const passingFees: number[] = JSON.parse(inputValues[2]);
	return minCost(maxTime, edges, passingFees);
}
