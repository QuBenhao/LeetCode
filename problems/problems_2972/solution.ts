function incremovableSubarrayCount(nums: number[]): number {
	const n: number = nums.length;
	let i: number = 0;
	while (i < n - 1 && nums[i] < nums[i + 1]) {
		i++;
	}
	if (i === n - 1) {
		return Math.floor(n * (n + 1) / 2);
	}
	let ans: number = i + 2;
	let j: number = n - 1;
	while (j == n - 1 || nums[j] < nums[j + 1]) {
		while (i >= 0 && nums[i] >= nums[j]) {
			i--;
		}
		ans += i + 2;
		j--;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return incremovableSubarrayCount(nums);
}
