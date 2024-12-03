function countCombinations(pieces: string[], positions: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const pieces: string[] = JSON.parse(inputValues[0]);
	const positions: number[][] = JSON.parse(inputValues[1]);
	return countCombinations(pieces, positions);
}
