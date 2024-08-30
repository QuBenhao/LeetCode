function canMakeSquare(grid: string[][]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: string[][] = JSON.parse(inputValues[0]);
	return canMakeSquare(grid);
}
