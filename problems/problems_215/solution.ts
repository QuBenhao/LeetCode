function findKthLargest(nums: number[], k: number): number {
    const pivot: number = nums[Math.floor(Math.random() * nums.length)];
	const left: number[] = [], right: number[] = [], equal: number[] = [];
	for (const num of nums) {
		if (num < pivot) {
			left.push(num);
		} else if (num > pivot) {
			right.push(num);
		} else {
			equal.push(num);
		}
	}
	if (k <= right.length) {
		return findKthLargest(right, k);
	} else if (k <= right.length + equal.length) {
		return pivot;
	} else {
		return findKthLargest(left, k - right.length - equal.length);
	}
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return findKthLargest(nums, k);
}
