function tictactoe(board: string[]): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const board: string[] = JSON.parse(inputValues[0]);
	return tictactoe(board);
}
