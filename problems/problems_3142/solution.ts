function satisfiesConditions(grid: number[][]): boolean {
    const m: number = grid.length, n: number = grid[0].length;
	for (let j: number = 0; j < n - 1; j++) {
		if (grid[0][j] == grid[0][j + 1]) {
			return false;
		}
	}
	for (let j: number = 0; j < n; j++) {
		const v: number = grid[0][j];
		for (let i: number = 1; i < m; i++) {
			if (grid[i][j] != v) {
				return false;
			}
		}
	}
	return true;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	return satisfiesConditions(grid);
}
