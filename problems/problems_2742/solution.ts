function paintWalls(cost: number[], time: number[]): number {

};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const cost: number[] = JSON.parse(splits[0]);
	const time: number[] = JSON.parse(splits[1]);
	return paintWalls(cost, time);
}
