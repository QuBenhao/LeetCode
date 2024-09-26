function isInterleave(s1: string, s2: string, s3: string): boolean {
	const m: number = s1.length, n: number = s2.length;
	if (m + n !== s3.length) {
		return false;
	}
	const dp: boolean[][] = new Array(m + 1).fill(false).map(() => new Array(n + 1).fill(false));
	dp[0][0] = true;
	for (let i: number = 1; i <= m && s1[i - 1] === s3[i - 1]; i++) {
		dp[i][0] = true;
	}
	for (let i: number = 1; i <= n && s2[i - 1] === s3[i - 1]; i++) {
		dp[0][i] = true;
	}
	for (let i: number = 1; i <= m; i++) {
		for (let j: number = 1; j <= n; j++) {
			dp[i][j] = (dp[i - 1][j] && s1[i - 1] === s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] === s3[i + j - 1]);
		}
	}
	return dp[m][n];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s1: string = JSON.parse(inputValues[0]);
	const s2: string = JSON.parse(inputValues[1]);
	const s3: string = JSON.parse(inputValues[2]);
	return isInterleave(s1, s2, s3);
}
