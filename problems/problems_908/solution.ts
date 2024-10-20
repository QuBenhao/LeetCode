function smallestRangeI(nums: number[], k: number): number {
    let min: number = nums[0], max: number = nums[0];
	for (const num of nums) {
		min = Math.min(min, num);
		max = Math.max(max, num);
	}
	return Math.max(0, max - min - 2 * k);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return smallestRangeI(nums, k);
}
