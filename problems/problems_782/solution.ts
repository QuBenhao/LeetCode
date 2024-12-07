function movesToChessboard(board: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const board: number[][] = JSON.parse(inputValues[0]);
	return movesToChessboard(board);
}
