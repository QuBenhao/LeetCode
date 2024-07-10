function permute(nums: number[]): number[][] {
	const ans: number[][] = [];
    const backtrack: Function = (idx: number): void => {
		if (idx === nums.length) {
			ans.push([...nums]);
			return;
		}
		for (let i: number = idx; i < nums.length; i++) {
			[nums[i], nums[idx]] = [nums[idx], nums[i]];
			backtrack(idx + 1);
			[nums[i], nums[idx]] = [nums[idx], nums[i]];
		}
	}
	backtrack(0);
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return permute(nums);
}
