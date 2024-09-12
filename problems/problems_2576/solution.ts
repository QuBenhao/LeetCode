function maxNumOfMarkedIndices(nums: number[]): number {
	nums.sort((a, b) => a - b);
	let left: number = 0;
	const n: number = nums.length;
	for (let right: number = Math.floor((n + 1) / 2); right < n; right++) {
		if (nums[right] >= 2 * nums[left]) {
			left++;
		}
	}
	return left * 2;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return maxNumOfMarkedIndices(nums);
}
