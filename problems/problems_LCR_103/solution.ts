function coinChange(coins: number[], amount: number): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const coins: number[] = JSON.parse(inputValues[0]);
	const amount: number = JSON.parse(inputValues[1]);
	return coinChange(coins, amount);
}
