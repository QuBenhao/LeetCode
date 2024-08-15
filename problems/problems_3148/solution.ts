function maxScore(grid: number[][]): number {
	let ans: number = Number.MIN_SAFE_INTEGER;
	const n: number = grid[0].length;
	const colsMin: Array<number> = new Array<number>(n).fill(Number.MAX_SAFE_INTEGER);
	for (const row of grid) {
		let preMin: number = Number.MAX_SAFE_INTEGER;
		for (let j: number = 0; j < n; j++) {
			ans = Math.max(ans, row[j] - Math.min(preMin, colsMin[j]));
			colsMin[j] = Math.min(colsMin[j], row[j]);
			preMin = Math.min(preMin, colsMin[j]);
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	return maxScore(grid);
}
