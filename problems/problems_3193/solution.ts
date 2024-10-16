function numberOfPermutations(n: number, requirements: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const requirements: number[][] = JSON.parse(inputValues[1]);
	return numberOfPermutations(n, requirements);
}
