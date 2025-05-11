function maximalRectangle(matrix: string[]): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const matrix: string[] = JSON.parse(inputValues[0]);
	return maximalRectangle(matrix);
}
