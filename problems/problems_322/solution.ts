function coinChange(coins: number[], amount: number): number {
	if (amount == 0) {
		return 0;
	}
	let dp: bigint = BigInt(1) << BigInt(amount);
	let step: number = 0;
	while (dp > 0) {
		let nxt: bigint = BigInt(0);
		step++;
		for (const coin of coins) {
			nxt |= dp >> BigInt(coin);
		}
		if ((nxt & BigInt(1)) === BigInt(1)) {
			return step;
		}
		dp = nxt;
	}
	return -1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const coins: number[] = JSON.parse(inputValues[0]);
	const amount: number = JSON.parse(inputValues[1]);
	return coinChange(coins, amount);
}
