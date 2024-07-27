function fallingSquares(positions: number[][]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const positions: number[][] = JSON.parse(inputValues[0]);
	return fallingSquares(positions);
}
