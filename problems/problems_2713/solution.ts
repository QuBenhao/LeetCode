function maxIncreasingCells(mat: number[][]): number {

};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const mat: number[][] = JSON.parse(splits[0]);
	return maxIncreasingCells(mat);
}
