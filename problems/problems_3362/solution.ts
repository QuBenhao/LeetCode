function maxRemoval(nums: number[], queries: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const queries: number[][] = JSON.parse(inputValues[1]);
	return maxRemoval(nums, queries);
}
