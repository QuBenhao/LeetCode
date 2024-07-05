/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
	let left: number = 0;
	for (let i: number = 0; i < nums.length; i++) {
		if (nums[i] != 0) {
			const tmp: number = nums[left];
			nums[left] = nums[i];
			nums[i] = tmp;
			left++;
		}
	}
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	moveZeroes(nums)
	return nums;
}
