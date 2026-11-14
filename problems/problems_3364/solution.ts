function minimumSumSubarray(nums: number[], l: number, r: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const l: number = JSON.parse(inputValues[1]);
	const r: number = JSON.parse(inputValues[2]);
	return minimumSumSubarray(nums, l, r);
}
