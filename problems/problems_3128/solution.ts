function numberOfRightTriangles(grid: number[][]): number {
	const m: number = grid.length, n: number = grid[0].length;
	const rowCount: number[] = new Array(m).fill(0), colCount: number[] = new Array(n).fill(0);
	for (let i: number = 0; i < m; i++) {
		for (let j: number = 0; j < n; j++) {
			if (grid[i][j] === 1) {
				rowCount[i]++;
				colCount[j]++;
			}
		}
	}
	let ans: number = 0;
	for (let i: number = 0; i < m; i++) {
		for (let j: number = 0; j < n; j++) {
			if (grid[i][j] === 1) {
				ans += (rowCount[i] - 1) * (colCount[j] - 1);
			}
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	return numberOfRightTriangles(grid);
}
