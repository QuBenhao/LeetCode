function maximumPoints(edges: number[][], coins: number[], k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const edges: number[][] = JSON.parse(inputValues[0]);
	const coins: number[] = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return maximumPoints(edges, coins, k);
}
