function uniquePaths(m: number, n: number): number {
	const dp: number[] = new Array(n).fill(1);
	for (let i: number = 1; i < m; i++) {
		for (let j: number = 1; j < n; j++) {
			dp[j] += dp[j - 1];
		}
	}
	return dp[n - 1];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const m: number = JSON.parse(inputValues[0]);
	const n: number = JSON.parse(inputValues[1]);
	return uniquePaths(m, n);
}
