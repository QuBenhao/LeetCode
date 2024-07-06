function checkMove(board: string[][], rMove: number, cMove: number, color: string): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const board: string[][] = JSON.parse(inputValues[0]);
	const rMove: number = JSON.parse(inputValues[1]);
	const cMove: number = JSON.parse(inputValues[2]);
	const color: string = JSON.parse(inputValues[3]);
	return checkMove(board, rMove, cMove, color);
}
