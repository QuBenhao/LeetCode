function modifiedMatrix(matrix: number[][]): number[][] {
	const m: number = matrix.length, n: number = matrix[0].length;
	for (let j = 0; j < n; j++) {
		let mx: number = -1;
		const remain: number[] = [];
		for (let i: number = 0; i < m; i++) {
			if (matrix[i][j] != -1) {
				mx = Math.max(mx, matrix[i][j]);
			} else {
				remain.push(i);
			}
		}
		for (const i of remain) {
			matrix[i][j] = mx;
		}
	}
	return matrix;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const matrix: number[][] = JSON.parse(inputValues[0]);
	return modifiedMatrix(matrix);
}
