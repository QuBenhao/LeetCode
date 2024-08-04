function findIntegers(n: number): number {
    const dp: Array<number> = new Array<number>(31);
	dp[0] = 1;
	dp[1] = 2;
	for (let i: number = 2; i < 31; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
	}
	n++;
	let ans: number = 0, pre: number = 0;
	for (let i = 29; i >= 0; i--) {
		if ((n & (1 << i)) !== 0) {
			ans += dp[i];
			if (pre === 1) {
				break;
			}
			pre = 1;
		} else {
			pre = 0;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return findIntegers(n);
}
