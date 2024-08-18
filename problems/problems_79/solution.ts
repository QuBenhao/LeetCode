function exist(board: string[][], word: string): boolean {
    const m: number = board.length, n: number = board[0].length, len: number = word.length;
	const directions: number[][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];
	const backTrack = (i: number, j: number, k: number): boolean => {
		if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[k]) {
			return false;
		}
		if (k == len - 1) {
			return true;
		}
		const temp: string = board[i][j];
		board[i][j] = "";
		for (const dir of directions) {
			if (backTrack(i + dir[0], j + dir[1], k + 1)) {
				return true;
			}
		}
		board[i][j] = temp;
		return false;
	}
	for (let i: number = 0; i < m; i++) {
		for (let j: number = 0; j < n; j++) {
			if (backTrack(i, j, 0)) {
				return true;
			}
		}
	}
	return false;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const board: string[][] = JSON.parse(inputValues[0]);
	const word: string = JSON.parse(inputValues[1]);
	return exist(board, word);
}
