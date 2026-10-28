function palindromePath(n: number, edges: number[][], s: string, queries: string[]): boolean[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	const s: string = JSON.parse(inputValues[2]);
	const queries: string[] = JSON.parse(inputValues[3]);
	return palindromePath(n, edges, s, queries);
}
