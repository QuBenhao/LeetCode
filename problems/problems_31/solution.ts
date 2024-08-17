/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    const swap: Function = (i: number, j: number) => {
		const temp: number = nums[i];
		nums[i] = nums[j];
		nums[j] = temp;
	};
	const reverse: Function = (start: number, end: number) => {
		while (start < end) {
			swap(start, end);
			start++;
			end--;
		}
	}
	const n: number = nums.length;
	let idx: number = n - 1;
	while (idx > 0 && nums[idx - 1] >= nums[idx]) {
		idx--;
	}
	if (idx === 0) {
		reverse(0, n - 1);
		return;
	}
	let swapIdx: number = n - 1;
	while (swapIdx >= idx && nums[swapIdx] <= nums[idx - 1]) {
		swapIdx--;
	}
	swap(idx - 1, swapIdx);
	reverse(idx, n - 1);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	nextPermutation(nums)
	return nums;
}
