function minimumMoney(transactions: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const transactions: number[][] = JSON.parse(inputValues[0]);
	return minimumMoney(transactions);
}
