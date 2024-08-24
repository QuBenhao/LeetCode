function maxProduct(nums: number[]): number {
    let ans: number = nums[0], max: number = nums[0], min: number = nums[0];
	for (let i = 1; i < nums.length; i++) {
		const temp: number = max;
		max = Math.max(max * nums[i], min * nums[i], nums[i]);
		min = Math.min(temp * nums[i], min * nums[i], nums[i]);
		ans = Math.max(ans, max);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return maxProduct(nums);
}
