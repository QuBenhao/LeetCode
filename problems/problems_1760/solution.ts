function minimumSize(nums: number[], maxOperations: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const maxOperations: number = JSON.parse(inputValues[1]);
	return minimumSize(nums, maxOperations);
}
