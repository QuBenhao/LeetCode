function checkMove(board: string[][], rMove: number, cMove: number, color: string): boolean {
	console.log("Color: " + color);
	const directions: number[][] = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]];
	const m: number = board.length, n: number = board[0].length;
	for (const dir of directions) {
		let x: number = rMove + dir[0], y: number = cMove + dir[1];
		if (x < 0 || x >= m || y < 0 || y >= n || board[x][y] == "." || board[x][y] == color) {
			continue;
		}
		while (x >= 0 && x < m && y >= 0 && y < n && board[x][y] != ".") {
			if (board[x][y] == color) {
				return true;
			}
			x += dir[0];
			y += dir[1];
		}
	}
	return false;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const board: string[][] = JSON.parse(inputValues[0]);
	const rMove: number = JSON.parse(inputValues[1]);
	const cMove: number = JSON.parse(inputValues[2]);
	const color: string = JSON.parse(inputValues[3]);
	return checkMove(board, rMove, cMove, color);
}
