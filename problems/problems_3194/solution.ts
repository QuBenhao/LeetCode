function minimumAverage(nums: number[]): number {
    const n: number = nums.length;
	nums.sort((a, b) => a - b);
	let ans: number = nums[0] + nums[n - 1];
	for (let i: number = 1; i < Math.floor(n / 2); i++) {
		ans = Math.min(ans, nums[i] + nums[n - i - 1]);
	}
	return ans / 2.0;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return minimumAverage(nums);
}
