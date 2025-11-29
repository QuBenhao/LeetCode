function minSubarray(nums: number[], p: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const p: number = JSON.parse(inputValues[1]);
	return minSubarray(nums, p);
}
