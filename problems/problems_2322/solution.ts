function minimumScore(nums: number[], edges: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	return minimumScore(nums, edges);
}
