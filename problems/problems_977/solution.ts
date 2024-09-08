function sortedSquares(nums: number[]): number[] {
	const n: number = nums.length;
	const ans: number[] = new Array(n);
	for (let left: number = 0, right: number = n - 1, pos: number = n - 1; left <= right; pos--) {
		if (Math.abs(nums[left]) > Math.abs(nums[right])) {
			ans[pos] = nums[left] * nums[left];
			left++;
		} else {
			ans[pos] = nums[right] * nums[right];
			right--;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return sortedSquares(nums);
}
