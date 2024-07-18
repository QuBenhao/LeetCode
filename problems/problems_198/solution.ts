function rob(nums: number[]): number {
    const dp: number[] = [0, nums[0]];
	for (let i: number = 1; i < nums.length; i++) {
		[dp[0], dp[1]] = [Math.max(dp[0], dp[1]), Math.max(dp[0] + nums[i], dp[1])];
	}
	return Math.max(dp[0], dp[1]);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return rob(nums);
}
