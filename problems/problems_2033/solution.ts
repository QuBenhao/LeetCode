function minOperations(grid: number[][], x: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	const x: number = JSON.parse(inputValues[1]);
	return minOperations(grid, x);
}
