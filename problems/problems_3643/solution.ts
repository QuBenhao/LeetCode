function reverseSubmatrix(grid: number[][], x: number, y: number, k: number): number[][] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	const x: number = JSON.parse(inputValues[1]);
	const y: number = JSON.parse(inputValues[2]);
	const k: number = JSON.parse(inputValues[3]);
	return reverseSubmatrix(grid, x, y, k);
}
