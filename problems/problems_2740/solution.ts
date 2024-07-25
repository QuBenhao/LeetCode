function findValueOfPartition(nums: number[]): number {
	let ans: number = Infinity;
	nums = nums.sort((a, b) => a - b);
	for (let i: number = 1; i < nums.length; i++) {
		ans = Math.min(ans, nums[i] - nums[i - 1]);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return findValueOfPartition(nums);
}
