function minCut(s: string): number {
	const n: number = s.length;
	const isPalindrome: boolean[][] = new Array(n).fill(null).map(() => new Array(n).fill(false));
	for (let i = 0; i < n; i++) {
		isPalindrome[i][i] = true;
		for (let j = 0; j < i; j++) {
			if (s[i] === s[j] && (i - j <= 1 || isPalindrome[j + 1][i - 1])) {
				isPalindrome[j][i] = true;
			}
		}
	}
	const dp: number[] = new Array(n).fill(Number.MAX_SAFE_INTEGER / 2);
	for (let i = 0; i < n; i++) {
		if (isPalindrome[0][i]) {
			dp[i] = 0;
		} else {
			for (let j = 0; j < i; j++) {
				if (isPalindrome[j + 1][i]) {
					dp[i] = Math.min(dp[i], dp[j] + 1);
				}
			}
		}
	}
	return dp[n - 1];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return minCut(s);
}
