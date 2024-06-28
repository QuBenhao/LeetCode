function firstMissingPositive(nums: number[]): number {
    const n: number = nums.length;
	for (let i: number = 0; i < n; i++) {
		if (nums[i] <= 0) {
			nums[i] = n + 1;
		}
	}
	for (let i: number = 0; i < n; i++) {
		const num: number = Math.abs(nums[i]);
		if (num <= n) {
			nums[num - 1] = -Math.abs(nums[num - 1]);
		}
	}
	for (let i: number = 0; i < n; i++) {
		if (nums[i] > 0) {
			return i + 1;
		}
	}
	return n + 1;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	return firstMissingPositive(nums);
}
