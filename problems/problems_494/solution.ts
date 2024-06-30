function findTargetSumWays(nums: number[], target: number): number {
	const t: number = target;
	nums.forEach(value => {
		target += value;
	});
	if (target % 2 != 0 || target < 0 || target < 2 * t) {
		return 0;
	}
	target >>= 1;
	const dp: number[] = new Array(target + 1).fill(0);
	dp[0] = 1;
	for (const num of nums) {
		for (let x: number = target; x >= num; x--) {
			dp[x] += dp[x - num];
		}
	}
	return dp[target];
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	const target: number = JSON.parse(splits[1]);
	return findTargetSumWays(nums, target);
}
