function longestCommonSubsequence(text1: string, text2: string): number {
    const m: number = text1.length, n: number = text2.length;
	const dp: Array<Array<number>> = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0));
	for (let i = 1; i <= m; i++) {
		for (let j = 1; j <= n; j++) {
			if (text1[i - 1] === text2[j - 1]) {
				dp[i][j] = dp[i - 1][j - 1] + 1;
			} else {
				dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
			}
		}
	}
	return dp[m][n];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const text1: string = JSON.parse(inputValues[0]);
	const text2: string = JSON.parse(inputValues[1]);
	return longestCommonSubsequence(text1, text2);
}
