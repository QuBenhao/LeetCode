function losingPlayer(x: number, y: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const x: number = JSON.parse(inputValues[0]);
	const y: number = JSON.parse(inputValues[1]);
	return losingPlayer(x, y);
}
