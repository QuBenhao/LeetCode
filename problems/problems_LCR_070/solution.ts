function singleNonDuplicate(nums: number[]): number {
	let left: number = 0, right: number = nums.length - 1;
	while (left < right) {
		const mid: number = left + Math.floor((right - left) / 2);
		if (nums[mid] == nums[mid ^ 1]) {
			left = (mid | 1) + 1;
		} else {
			right = mid;
		}
	}
	return nums[left];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return singleNonDuplicate(nums);
}
