/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    for (let i: number = 0, p0: number = 0, p1: number = 0; i < nums.length; i++) {
		if (nums[i] == 1) {
			swap(nums, p1, i);
			p1++;
		} else if (nums[i] == 0) {
			swap(nums, p0, i);
			if (p0 < p1) {
				swap(nums, p1, i);
			}
			p0++;
			p1++;
		}
	}
};

function swap(nums: number[], i: number, j: number): void {
	const tmp: number = nums[i];
	nums[i] = nums[j];
	nums[j] = tmp;
}

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	sortColors(nums)
	return nums;
}
