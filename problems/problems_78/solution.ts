function subsets(nums: number[]): number[][] {
    const dfs = (arr: number[], idx: number): void => {
		if (idx == nums.length) {
			ans.push([...arr]);
			return;
		}
		dfs(arr, idx + 1);
		arr.push(nums[idx]);
		dfs(arr, idx + 1);
		arr.pop();
	}

	const ans: number[][] = [];
	dfs([], 0);
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	return subsets(nums);
}
