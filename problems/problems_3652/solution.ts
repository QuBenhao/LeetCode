function maxProfit(prices: number[], strategy: number[], k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const prices: number[] = JSON.parse(inputValues[0]);
	const strategy: number[] = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return maxProfit(prices, strategy, k);
}
