function minimumValueSum(nums: number[], andValues: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const andValues: number[] = JSON.parse(inputValues[1]);
	return minimumValueSum(nums, andValues);
}
