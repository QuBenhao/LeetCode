function resultArray(nums: number[], k: number, queries: number[][]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const queries: number[][] = JSON.parse(inputValues[2]);
	return resultArray(nums, k, queries);
}
