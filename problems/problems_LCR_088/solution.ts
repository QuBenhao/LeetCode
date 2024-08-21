function minCostClimbingStairs(cost: number[]): number {
	const n: number = cost.length;
	const dp: number[] = new Array(3).fill(0);
	for (let i: number = 2; i < n + 1; i++) {
		dp[i % 3] = Math.min(dp[(i - 1) % 3] + cost[i - 1], dp[(i - 2) % 3] + cost[i - 2]);
	}
	return dp[n % 3];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const cost: number[] = JSON.parse(inputValues[0]);
	return minCostClimbingStairs(cost);
}
