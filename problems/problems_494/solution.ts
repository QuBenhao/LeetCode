function findTargetSumWays(nums: number[], target: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	const target: number = JSON.parse(splits[1]);
	return findTargetSumWays(nums, target);
}
