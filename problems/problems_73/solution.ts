/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
	const m: number = matrix.length, n: number = matrix[0].length;
	let row0: boolean = false, col0: boolean = false;
	for (let i: number = 0; i < m; i++) {
		if (matrix[i][0] == 0) {
			col0 = true;
		}
	}
	for (let j: number = 0; j < n; j++) {
		if (matrix[0][j] == 0) {
			row0 = true;
		}
	}
	for (let i: number = 1; i < m; i++) {
		for (let j: number = 1; j < n; j++) {
			if (matrix[i][j] == 0) {
				matrix[i][0] = matrix[0][j] = 0;
			}
		}
	}
	for (let i: number = 1; i < m; i++) {
		for (let j: number = 1; j < n; j++) {
			if (matrix[i][0] == 0 || matrix[0][j] == 0) {
				matrix[i][j] = 0;
			}
		}
	}
	if (row0) {
		for (let j: number = 0; j < n; j++) {
			matrix[0][j] = 0;
		}
	}
	if (col0) {
		for (let i: number = 0; i < m; i++) {
			matrix[i][0] = 0;
		}
	}
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const matrix: number[][] = JSON.parse(inputValues[0]);
	setZeroes(matrix)
	return matrix;
}
