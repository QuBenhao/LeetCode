function isArraySpecial(nums: number[], queries: number[][]): boolean[] {
	const n: number = nums.length;
	const preSum: Array<number> = new Array<number>(n).fill(0);
	for (let i: number = 0; i < n - 1; i++) {
		preSum[i + 1] = preSum[i] + ((nums[i] & 1) !== (nums[i + 1] & 1) ? 1 : 0);
	}
	const ans: boolean[] = new Array<boolean>(queries.length);
	for (let i: number = 0; i < queries.length; i++) {
		const [l, r] = queries[i];
		ans[i] = preSum[r] - preSum[l] === r - l;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const queries: number[][] = JSON.parse(inputValues[1]);
	return isArraySpecial(nums, queries);
}
