function minimumMoves(nums: number[], k: number, maxChanges: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const maxChanges: number = JSON.parse(inputValues[2]);
	return minimumMoves(nums, k, maxChanges);
}
