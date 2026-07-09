function pathExistenceQueries(n: number, nums: number[], maxDiff: number, queries: number[][]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const nums: number[] = JSON.parse(inputValues[1]);
	const maxDiff: number = JSON.parse(inputValues[2]);
	const queries: number[][] = JSON.parse(inputValues[3]);
	return pathExistenceQueries(n, nums, maxDiff, queries);
}
