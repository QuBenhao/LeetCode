function earliestAndLatest(n: number, firstPlayer: number, secondPlayer: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const firstPlayer: number = JSON.parse(inputValues[1]);
	const secondPlayer: number = JSON.parse(inputValues[2]);
	return earliestAndLatest(n, firstPlayer, secondPlayer);
}
