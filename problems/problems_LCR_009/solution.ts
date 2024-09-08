function numSubarrayProductLessThanK(nums: number[], k: number): number {
	let ans: number = 0, cur: number = 1;
	const n: number = nums.length;
	for (let left: number = 0, right: number = 0; right < n; right++) {
		cur *= nums[right];
		while (left <= right && cur >= k) {
			cur /= nums[left];
			left++;
		}
		ans += right - left + 1;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return numSubarrayProductLessThanK(nums, k);
}
