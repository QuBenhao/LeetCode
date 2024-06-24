function nextGreaterElements(nums: number[]): number[] {
	const n: number = nums.length;
	const ans: number[] = new Array(n).fill(-1);
	const stack: number[] = [];
	for (let i: number = 0; i < n * 2; i++) {
		while (stack.length > 0 && nums[stack[stack.length - 1]] < nums[i % n]) {
			ans[stack[stack.length - 1]] = nums[i % n];
			stack.pop();
		}
		if (i < n) {
			stack.push(i);
		} else if (stack.length == 0) {
			break;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	return nextGreaterElements(nums);
}
