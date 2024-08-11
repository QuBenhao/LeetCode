function maxUncrossedLines(nums1: number[], nums2: number[]): number {
	const m: number = nums1.length, n: number = nums2.length;
	const dp: number[][] = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0));
	for (let i: number = 1; i <= m; i++) {
		for (let j: number = 1; j <= n; j++) {
			if (nums1[i - 1] === nums2[j - 1]) {
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
	const nums1: number[] = JSON.parse(inputValues[0]);
	const nums2: number[] = JSON.parse(inputValues[1]);
	return maxUncrossedLines(nums1, nums2);
}
