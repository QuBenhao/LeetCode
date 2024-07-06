function numIslands(grid: string[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: string[][] = JSON.parse(inputValues[0]);
	return numIslands(grid);
}
