function countUnguarded(m: number, n: number, guards: number[][], walls: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const m: number = JSON.parse(inputValues[0]);
	const n: number = JSON.parse(inputValues[1]);
	const guards: number[][] = JSON.parse(inputValues[2]);
	const walls: number[][] = JSON.parse(inputValues[3]);
	return countUnguarded(m, n, guards, walls);
}
