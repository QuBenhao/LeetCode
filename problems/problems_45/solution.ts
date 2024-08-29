function jump(nums: number[]): number {
    let ans: number = 0;
	const n: number = nums.length;
	for (let cur: number = 0, nxt: number = 0; nxt < n - 1; ans++) {
		let tmp: number = nxt;
		for (let i: number = cur; i <= nxt; i++) {
			tmp = Math.max(tmp, nums[i] + i);
		}
		cur = nxt + 1;
		nxt = tmp;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return jump(nums);
}
