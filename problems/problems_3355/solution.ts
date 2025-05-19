function isZeroArray(nums: number[], queries: number[][]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const queries: number[][] = JSON.parse(inputValues[1]);
	return isZeroArray(nums, queries);
}
