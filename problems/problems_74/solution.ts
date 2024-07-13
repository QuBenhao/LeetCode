function searchMatrix(matrix: number[][], target: number): boolean {
	const m: number = matrix.length, n: number = matrix[0].length;
	let row: number = 0, col: number = n - 1;
	while (row < m && col >= 0) {
		if (matrix[row][col] === target) return true;
		if (matrix[row][col] < target) row++;
		else col--;
	}
	return false;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const matrix: number[][] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return searchMatrix(matrix, target);
}
