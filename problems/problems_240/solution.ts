function searchMatrix(matrix: number[][], target: number): boolean {
	const m: number = matrix.length, n: number = matrix[0].length;
	let row: number = m - 1, col: number = 0;
	while (row >= 0 && col < n) {
		if (matrix[row][col] == target) {
			return true;
		} else if (matrix[row][col] > target) {
			row--;
		} else {
			col++;
		}
	}
	return false;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const matrix: number[][] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return searchMatrix(matrix, target);
}
