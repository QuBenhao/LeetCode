function solveNQueens(n: number): string[][] {
	const board: string[][] = Array.from({ length: n }, () => Array.from({ length: n }, () => "."));
	const result: string[][] = [];
	const cols: boolean[] = Array.from({ length: n }, () => false);
	const diag1: boolean[] = Array.from({ length: 2 * n - 1 }, () => false);
	const diag2: boolean[] = Array.from({ length: 2 * n - 1 }, () => false);
	const backtrack = (row: number) => {
		if (row === n) {
			result.push(board.map((r) => r.join("")));
			return;
		}
		for (let col = 0; col < n; col++) {
			if (!cols[col] && !diag1[row + col] && !diag2[row - col + n - 1]) {
				cols[col] = diag1[row + col] = diag2[row - col + n - 1] = true;
				board[row][col] = "Q";
				backtrack(row + 1);
				board[row][col] = ".";
				cols[col] = diag1[row + col] = diag2[row - col + n - 1] = false;
			}
		}
	};
	backtrack(0);
	return result;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return solveNQueens(n);
}
