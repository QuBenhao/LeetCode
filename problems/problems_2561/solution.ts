function minCost(basket1: number[], basket2: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const basket1: number[] = JSON.parse(inputValues[0]);
	const basket2: number[] = JSON.parse(inputValues[1]);
	return minCost(basket1, basket2);
}
