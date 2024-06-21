function findMissingRanges(nums: number[], lower: number, upper: number): number[][] {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	const lower: number = JSON.parse(splits[1]);
	const upper: number = JSON.parse(splits[2]);
	return findMissingRanges(nums, lower, upper);
}
