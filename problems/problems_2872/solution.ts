function maxKDivisibleComponents(n: number, edges: number[][], values: number[], k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	const values: number[] = JSON.parse(inputValues[2]);
	const k: number = JSON.parse(inputValues[3]);
	return maxKDivisibleComponents(n, edges, values, k);
}
