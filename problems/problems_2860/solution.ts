function countWays(nums: number[]): number {
	const n: number = nums.length;
	nums.sort((a, b) => a - b);
	let ans: number = nums[0] > 0 ? 2 : 1;
	for (let i: number = 1; i < n; i++) {
		if (nums[i - 1] < i && nums[i] > i) {
			ans++;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return countWays(nums);
}
