function isValidSudoku(board: string[][]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const board: string[][] = JSON.parse(inputValues[0]);
	return isValidSudoku(board);
}
