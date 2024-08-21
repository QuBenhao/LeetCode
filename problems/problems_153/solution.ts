function findMin(nums: number[]): number {
	let left: number = 0, right: number = nums.length - 1;
	while (left < right) {
		if (nums[left] < nums[right]) {
			return nums[left];
		}
		const mid: number = left + Math.floor((right - left) / 2);
		if (nums[mid] < nums[right]) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return nums[left];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return findMin(nums);
}
