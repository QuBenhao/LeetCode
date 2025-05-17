function colorTheGrid(m: number, n: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const m: number = JSON.parse(inputValues[0]);
	const n: number = JSON.parse(inputValues[1]);
	return colorTheGrid(m, n);
}
