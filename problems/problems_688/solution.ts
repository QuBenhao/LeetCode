function knightProbability(n: number, k: number, row: number, column: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const row: number = JSON.parse(inputValues[2]);
	const column: number = JSON.parse(inputValues[3]);
	return knightProbability(n, k, row, column);
}
