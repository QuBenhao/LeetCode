function minimumDifference(nums: number[], k: number): number {
    const n: number = nums.length;
	let ans: number = Math.abs(nums[0] - k);
	for (let i: number = 1; i < n; i++) {
		ans = Math.min(ans, Math.abs(nums[i] - k));
		for (let j: number = i - 1; j >= 0 && (nums[j] | nums[i]) != nums[j]; j--) {
			nums[j] |= nums[i];
			ans = Math.min(ans, Math.abs(nums[j] - k));
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return minimumDifference(nums, k);
}
