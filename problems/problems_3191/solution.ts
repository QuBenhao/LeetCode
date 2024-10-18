function minOperations(nums: number[]): number {
    const n: number = nums.length;
	let ans: number = 0;
	for (let i: number = 0; i < n - 2; i++) {
		if (nums[i] === 0) {
			ans++;
			nums[i + 1] ^= 1;
			nums[i + 2] ^= 1;
		}
	}
	return nums[n - 2] === 1 && nums[n - 1] === 1 ? ans : -1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return minOperations(nums);
}
