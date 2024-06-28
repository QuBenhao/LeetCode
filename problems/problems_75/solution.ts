/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	return sortColors(nums);
}
