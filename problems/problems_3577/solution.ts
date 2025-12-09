function countPermutations(complexity: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const complexity: number[] = JSON.parse(inputValues[0]);
	return countPermutations(complexity);
}
