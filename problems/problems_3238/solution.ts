function winningPlayerCount(n: number, pick: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const pick: number[][] = JSON.parse(inputValues[1]);
	return winningPlayerCount(n, pick);
}
