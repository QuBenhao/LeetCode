function permute(nums: number[]): number[][] {
	const res: number[][] = [];
	const backtrack = (path: number[]) => {
		if (path.length === nums.length) {
			res.push(path.slice());
			return;
		}
		for (const num of nums) {
			if (path.includes(num)) {
				continue;
			}
			path.push(num);
			backtrack(path);
			path.pop();
		}
	};
	backtrack([]);
	return res;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return permute(nums);
}
