function mincostTickets(days: number[], costs: number[]): number {
    const n: number = days.length;
	const dp: number[] = new Array<number>(n + 1).fill(0);
	for (let i: number = 0, j: number = 0, k: number = 0; i < n; i++) {
		while (days[j] <= days[i] - 7) j++;
		while (days[k] <= days[i] - 30) k++;
		dp[i + 1] = Math.min(dp[j] + costs[1], dp[k] + costs[2], dp[i] + costs[0]);
	}
	return dp[n];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const days: number[] = JSON.parse(inputValues[0]);
	const costs: number[] = JSON.parse(inputValues[1]);
	return mincostTickets(days, costs);
}
