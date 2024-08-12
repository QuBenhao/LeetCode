/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
	const reverse: Function = (start: number, end: number): void => {
		while (start < end) {
			const temp: number = nums[start];
			nums[start] = nums[end];
			nums[end] = temp;
			start++;
			end--;
		}
	};
	const n: number = nums.length;
	k %= n;
	reverse(0, n - 1);
	reverse(0, k - 1);
	reverse(k, n - 1);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	rotate(nums, k)
	return nums;
}
