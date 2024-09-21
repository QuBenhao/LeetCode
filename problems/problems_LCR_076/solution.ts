function findKthLargest(nums: number[], k: number): number {
	nums.sort((a, b) => b - a);
	return nums[k - 1];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return findKthLargest(nums, k);
}
