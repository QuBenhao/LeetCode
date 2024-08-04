function search(nums: number[], target: number): number {
    let left: number = 0, right: number = nums.length - 1;
	while (left < right) {
		const mid: number = left + Math.floor((right - left) / 2);
		if (nums[mid] < nums[0]) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	if (target >= nums[0]) {
		right = left;
		left = 0;
	} else {
		right = nums.length - 1;
	}
	while (left < right) {
		const mid: number = left + Math.floor((right - left) / 2);
		if (nums[mid] < target) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return nums[left] === target ? left : -1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return search(nums, target);
}
