function minimumCost(cost: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const cost: number[] = JSON.parse(inputValues[0]);
	return minimumCost(cost);
}
