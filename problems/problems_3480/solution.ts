function maxSubarrays(n: number, conflictingPairs: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const conflictingPairs: number[][] = JSON.parse(inputValues[1]);
	return maxSubarrays(n, conflictingPairs);
}
