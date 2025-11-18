function findFinalValue(nums: number[], original: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const original: number = JSON.parse(inputValues[1]);
	return findFinalValue(nums, original);
}
