function nextGreaterElements(nums: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	return nextGreaterElements(nums);
}
