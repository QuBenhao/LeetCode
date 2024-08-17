function exist(board: string[][], word: string): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const board: string[][] = JSON.parse(inputValues[0]);
	const word: string = JSON.parse(inputValues[1]);
	return exist(board, word);
}
