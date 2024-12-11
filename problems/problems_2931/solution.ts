function maxSpending(values: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const values: number[][] = JSON.parse(inputValues[0]);
	return maxSpending(values);
}
