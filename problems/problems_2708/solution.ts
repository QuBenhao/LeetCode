function maxStrength(nums: number[]): number {
	let max: number = nums[0], min: number = nums[0];
	for (let i: number = 1; i < nums.length; i++) {
		const tmp: number = max, num: number = nums[i];
		max = Math.max(Math.max(Math.max(max * num, min * num), num), max);
		min = Math.min(Math.min(Math.min(min * num, tmp * num), num), min);
	}
	return max;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return maxStrength(nums);
}
