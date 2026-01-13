function separateSquares(squares: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const squares: number[][] = JSON.parse(inputValues[0]);
	return separateSquares(squares);
}
