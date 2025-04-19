function countFairPairs(nums: number[], lower: number, upper: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const lower: number = JSON.parse(inputValues[1]);
	const upper: number = JSON.parse(inputValues[2]);
	return countFairPairs(nums, lower, upper);
}
