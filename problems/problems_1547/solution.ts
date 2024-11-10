function minCost(n: number, cuts: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const cuts: number[] = JSON.parse(inputValues[1]);
	return minCost(n, cuts);
}
