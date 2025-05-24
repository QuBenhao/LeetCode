function longestIncreasingPath(matrix: number[][]): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const matrix: number[][] = JSON.parse(inputValues[0]);
	return longestIncreasingPath(matrix);
}
