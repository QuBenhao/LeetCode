function productExceptSelf(nums: number[]): number[] {
    const n: number = nums.length;
	const ans: number[] = new Array(n).fill(1);
	for (let i: number = 1; i < n; i++) {
		ans[i] = ans[i - 1] * nums[i - 1];
	}
	let right: number = 1;
	for (let i: number = n - 1; i >= 0; i--) {
		ans[i] *= right;
		right *= nums[i];
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return productExceptSelf(nums);
}
