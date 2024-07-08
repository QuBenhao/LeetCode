function climbStairs(n: number): number {
	const dp: number[] = new Array(3);
	dp[1] = 1;
	dp[2] = 2;
	for (let i: number = 3; i <= n; i++) {
		dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3];
	}
	return dp[n % 3];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return climbStairs(n);
}
