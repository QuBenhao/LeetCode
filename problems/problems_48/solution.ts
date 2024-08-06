/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
	const n: number = matrix.length;
	for (let i: number = 0; i < Math.floor(n / 2); i++) {
		for (let j: number = 0; j < Math.floor((n + 1) / 2); j++) {
			const temp: number = matrix[i][j];
			matrix[i][j] = matrix[n - j - 1][i];
			matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
			matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
			matrix[j][n - i - 1] = temp;
		}
	}
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const matrix: number[][] = JSON.parse(inputValues[0]);
	rotate(matrix)
	return matrix;
}
