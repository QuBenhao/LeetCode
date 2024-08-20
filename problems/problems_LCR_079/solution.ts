function subsets(nums: number[]): number[][] {
	const ans: number[][] = [];
	const backtrack: Function = (idx: number, path: number[]): void => {
		if (idx === nums.length) {
			ans.push([...path]);
			return;
		}
		backtrack(idx + 1, path);
		path.push(nums[idx]);
		backtrack(idx + 1, path);
		path.pop();
	}
	backtrack(0, []);
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return subsets(nums);
}
