function minimumCoins(prices: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const prices: number[] = JSON.parse(inputValues[0]);
	return minimumCoins(prices);
}
