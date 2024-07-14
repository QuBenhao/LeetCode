function maxIncreaseKeepingSkyline(grid: number[][]): number {
	const n: number = grid.length;
	const rowMax: number[] = new Array(n).fill(0), colMax: number[] = new Array(n).fill(0);
	for (let i: number = 0; i < n; i++) {
		for (let j: number = 0; j < n; j++) {
			rowMax[i] = Math.max(rowMax[i], grid[i][j]);
			colMax[j] = Math.max(colMax[j], grid[i][j]);
		}
	}
	let result: number = 0;
	for (let i: number = 0; i < n; i++) {
		for (let j: number = 0; j < n; j++) {
			result += Math.min(rowMax[i], colMax[j]) - grid[i][j];
		}
	}
	return result;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	return maxIncreaseKeepingSkyline(grid);
}
