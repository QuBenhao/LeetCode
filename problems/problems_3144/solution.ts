function minimumSubstringsInPartition(s: string): number {
    const n: number = s.length;
	const dp: number[] = new Array(n + 1).fill(n);
	dp[0] = 0;
	for (let i: number = 0; i < n; i++) {
		const cnt: number[] = new Array(26).fill(0);
		let maxCnt: number = 0;
		let count: number = 0;
		for (let j: number = i; j >= 0; j--) {
			const c: number = s.charCodeAt(j) - "a".charCodeAt(0);
			if (++cnt[c] === 1) {
				count++;
			}
			maxCnt = Math.max(maxCnt, cnt[c]);
			if (i - j + 1 == maxCnt * count) {
				dp[i + 1] = Math.min(dp[i + 1], dp[j] + 1);
			}
		}
	}
	return dp[n];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return minimumSubstringsInPartition(s);
}
