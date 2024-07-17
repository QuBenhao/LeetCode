function minimumTime(n: number, edges: number[][], disappear: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	const disappear: number[] = JSON.parse(inputValues[2]);
	return minimumTime(n, edges, disappear);
}
