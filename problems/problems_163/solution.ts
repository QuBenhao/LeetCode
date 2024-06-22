function findMissingRanges(nums: number[], lower: number, upper: number): number[][] {
	const ans: number[][] = [];
	nums.push(upper + 1);
	let last: number = lower - 1;
	for (const num of nums) {
		if (num - last > 1) {
			ans.push([last + 1, num - 1]);
		}
		last = num;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	const lower: number = JSON.parse(splits[1]);
	const upper: number = JSON.parse(splits[2]);
	return findMissingRanges(nums, lower, upper);
}
