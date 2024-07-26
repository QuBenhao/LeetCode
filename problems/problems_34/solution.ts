function searchRange(nums: number[], target: number): number[] {
    const bisectLeft = (target: number): number => {
		let left: number = 0, right: number = nums.length;
		while (left < right) {
			const mid: number = Math.floor((left + right) / 2);
			if (nums[mid] >= target) {
				right = mid;
			} else {
				left = mid + 1;
			}
		}
		return left;
	}
	const bisectRight = (target: number): number => {
		let left: number = 0, right: number = nums.length;
		while (left < right) {
			const mid: number = Math.floor((left + right) / 2);
			if (nums[mid] > target) {
				right = mid;
			} else {
				left = mid + 1;
			}
		}
		return left;
	}
	const left: number = bisectLeft(target);
	const right: number = bisectRight(target) - 1;
	if (left <= right && nums[left] === target) {
		return [left, right];
	}
	return [-1, -1];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return searchRange(nums, target);
}
