function maxAreaOfIsland(grid: number[][]): number {
	const directions: number[][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];
	const m: number = grid.length, n: number = grid[0].length;
	const dfs = (i: number, j: number): number => {
		if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] === 0) {
			return 0;
		}
		grid[i][j] = 0;
		let res: number = 1;
		for (const direction of directions) {
			res += dfs(i + direction[0], j + direction[1]);
		}
		return res;
	}
	let result: number = 0;
	for (let i: number = 0; i < m; i++) {
		for (let j: number = 0; j < n; j++) {
			if (grid[i][j] === 1) {
				result = Math.max(result, dfs(i, j));
			}
		}
	}
	return result;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	return maxAreaOfIsland(grid);
}
