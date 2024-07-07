function numIslands(grid: string[][]): number {
	const m: number = grid.length, n: number = grid[0].length;
	const directions: number[][] = [[0, 1], [1, 0], [0, -1], [-1, 0]];
	const dfs: Function = (r: number, c: number): void => {
		if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == "0") {
			return;
		}
		grid[r][c] = "0";
		for (const dir of directions) {
			dfs(r + dir[0], c + dir[1]);
		}
	}
	let ans: number = 0;
	for (let i: number = 0; i < m; i++) {
		for (let j: number = 0; j < n; j++) {
			if (grid[i][j] == "1") {
				ans++;
				dfs(i, j);
			}
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: string[][] = JSON.parse(inputValues[0]);
	return numIslands(grid);
}
