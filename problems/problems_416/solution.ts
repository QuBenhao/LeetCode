function canPartition(nums: number[]): boolean {
    let sum: number = 0;
	for (const num of nums) {
		sum += num;
	}
	if (sum % 2 !== 0) {
		return false;
	}
	const target: number = sum / 2;
	const dp: boolean[] = new Array(target + 1).fill(false);
	dp[0] = true;
	for (const num of nums) {
		for (let i = target; i >= num; i--) {
			dp[i] = dp[i] || dp[i - num];
		}
	}
	return dp[target];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return canPartition(nums);
}
