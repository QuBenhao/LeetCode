function differenceOfDistinctValues(grid: number[][]): number[][] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	return differenceOfDistinctValues(grid);
}
