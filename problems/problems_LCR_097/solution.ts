function numDistinct(s: string, t: string): number {
	const m: number = s.length, n: number = t.length;
	const dp: number[][] = Array.from({length: m + 1}, () => Array(n + 1).fill(0));
	for (let i: number = 0; i <= m; i++) {
		dp[i][0] = 1;
	}
	for (let i: number = 1; i <= m; i++) {
		for (let j: number = 1; j <= n; j++) {
			if (s[i - 1] == t[j - 1]) {
				dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
			} else {
				dp[i][j] = dp[i - 1][j];
			}
		}
	}
	return dp[m][n];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const t: string = JSON.parse(inputValues[1]);
	return numDistinct(s, t);
}
