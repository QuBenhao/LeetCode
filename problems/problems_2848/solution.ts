function numberOfPoints(nums: number[][]): number {
	nums.sort((a, b) => a[0] - b[0]);
	let ans: number = 0, cur: number = nums[0][0] - 1;
	for (const [l, r] of nums) {
		if (cur < l) {
			cur = r;
			ans += r - l + 1;
		} else if (cur < r) {
			ans += r - cur;
			cur = r;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[][] = JSON.parse(inputValues[0]);
	return numberOfPoints(nums);
}
