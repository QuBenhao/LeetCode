function maximalPathQuality(values: number[], edges: number[][], maxTime: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const values: number[] = JSON.parse(splits[0]);
	const edges: number[][] = JSON.parse(splits[1]);
	const maxTime: number = JSON.parse(splits[2]);
	return maximalPathQuality(values, edges, maxTime);
}
