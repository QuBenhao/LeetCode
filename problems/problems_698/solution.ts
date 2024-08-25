function canPartitionKSubsets(nums: number[], k: number): boolean {
	const n: number = nums.length;
	let sum: number = 0;
	for (const num of nums) {
		sum += num;
	}
	if (sum % k != 0) {
		return false;
	}
	const target: number = Math.floor(sum / k);
	for (const num of nums) {
		if (num > target) {
			return false;
		}
	}
	const allPicked: number = (1 << n) - 1;
	const dp: number[] = new Array(1 << n).fill(-1);
	dp[0] = 0;
	for (let mask: number = 0; mask < (1 << n); mask++) {
		for (let i: number = 0; i < n; i++) {
			if (((mask >> i) & 1) !== 0) {
				const before: number = mask ^ (1 << i);
				if (dp[before] !== -1 && dp[before] + nums[i] <= target) {
					dp[mask] = (dp[before] + nums[i]) % target;
				}
			}
		}
	}
	return dp[allPicked] === 0;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return canPartitionKSubsets(nums, k);
}
