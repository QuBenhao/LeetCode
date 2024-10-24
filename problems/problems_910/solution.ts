function smallestRangeII(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let ans = nums.at(-1)! - nums[0];
    for (let i = 1; i < nums.length; ++i) {
        const mi = Math.min(nums[0] + k, nums[i] - k);
        const mx = Math.max(nums.at(-1)! - k, nums[i - 1] + k);
        ans = Math.min(ans, mx - mi);
    }
    return ans;
}

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return smallestRangeII(nums, k);
}
