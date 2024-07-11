function numberGame(nums: number[]): number[] {
	nums.sort((a, b) => a - b);
	const n: number = nums.length;
	for (let i: number = 0; i < n; i += 2) {
		[nums[i], nums[i + 1]] = [nums[i + 1], nums[i]]
	}
	return nums;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return numberGame(nums);
}
