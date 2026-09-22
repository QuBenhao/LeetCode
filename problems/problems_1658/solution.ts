function minOperations(nums: number[], x: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const x: number = JSON.parse(inputValues[1]);
	return minOperations(nums, x);
}
