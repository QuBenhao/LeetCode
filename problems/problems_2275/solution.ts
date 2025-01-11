function largestCombination(candidates: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const candidates: number[] = JSON.parse(inputValues[0]);
	return largestCombination(candidates);
}
