function findSmallestInteger(nums: number[], value: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const value: number = JSON.parse(inputValues[1]);
	return findSmallestInteger(nums, value);
}
