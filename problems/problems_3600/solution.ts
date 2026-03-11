function maxStability(n: number, edges: number[][], k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return maxStability(n, edges, k);
}
