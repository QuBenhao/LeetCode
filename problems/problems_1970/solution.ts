function latestDayToCross(row: number, col: number, cells: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const row: number = JSON.parse(inputValues[0]);
	const col: number = JSON.parse(inputValues[1]);
	const cells: number[][] = JSON.parse(inputValues[2]);
	return latestDayToCross(row, col, cells);
}
