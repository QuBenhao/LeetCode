function pathsWithMaxScore(board: string[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const board: string[] = JSON.parse(inputValues[0]);
	return pathsWithMaxScore(board);
}
