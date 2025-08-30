/**
 Do not return anything, modify board in-place instead.
 */
function solveSudoku(board: string[][]): void {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const board: string[][] = JSON.parse(inputValues[0]);
	solveSudoku(board)
	return board;
}
