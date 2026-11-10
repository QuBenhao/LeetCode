function minimumCost(cost1: number, cost2: number, costBoth: number, need1: number, need2: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const cost1: number = JSON.parse(inputValues[0]);
	const cost2: number = JSON.parse(inputValues[1]);
	const costBoth: number = JSON.parse(inputValues[2]);
	const need1: number = JSON.parse(inputValues[3]);
	const need2: number = JSON.parse(inputValues[4]);
	return minimumCost(cost1, cost2, costBoth, need1, need2);
}
