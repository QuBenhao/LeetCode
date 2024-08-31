function canMakeSquare(grid: string[][]): boolean {
	const m: number = grid.length, n: number = grid[0].length;
	for (let i: number = 0; i < m - 1; i++) {
		for (let j: number = 0; j < n - 1; j++) {
			let count: number = 0;
			for (let r: number = i; r < i + 2; r++) {
				for (let c: number = j; c < j + 2; c++) {
					if (grid[r][c] === "B") {
						count++;
					}
				}
			}
			if (count != 2) {
				return true;
			}
		}
	}
	return false;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: string[][] = JSON.parse(inputValues[0]);
	return canMakeSquare(grid);
}
