function goodSubsetofBinaryMatrix(grid: number[][]): number[] {

};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(splits[0]);
	return goodSubsetofBinaryMatrix(grid);
}
