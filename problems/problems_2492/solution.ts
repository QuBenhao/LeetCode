function minScore(n: number, roads: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const roads: number[][] = JSON.parse(inputValues[1]);
	return minScore(n, roads);
}
