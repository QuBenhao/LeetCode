function maximizeWin(prizePositions: number[], k: number): number {
	const n: number = prizePositions.length;
	const dp: number[] = new Array(n + 1).fill(0);
	let ans: number = 0;
	for (let left: number = 0, right: number = 0; right < n; right++) {
		while (prizePositions[right] - prizePositions[left] > k) {
			left++;
		}
		ans = Math.max(ans, dp[left] + right - left + 1);
		dp[right + 1] = Math.max(dp[right], right - left + 1);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const prizePositions: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return maximizeWin(prizePositions, k);
}
