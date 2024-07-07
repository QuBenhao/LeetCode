function searchInsert(nums: number[], target: number): number {
    let left: number = 0, right: number = nums.length;
	while (left < right) {
		const mid: number = left + Math.floor((right - left) / 2);
		if (nums[mid] < target) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return searchInsert(nums, target);
}
