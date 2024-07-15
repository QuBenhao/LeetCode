function minPathSum(grid: number[][]): number {
	const m: number = grid.length, n: number = grid[0].length;
	const dp: number[] = new Array(n).fill(0);
	for (let i: number = 0; i < m; i++) {
		dp[0] += grid[i][0];
		for (let j: number = 1; j < n; j++) {
			dp[j] = (i === 0 ? dp[j - 1] : Math.min(dp[j - 1], dp[j])) + grid[i][j];
		}
	}
	return dp[n - 1];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	return minPathSum(grid);
}
