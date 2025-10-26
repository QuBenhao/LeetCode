function numberOfBeams(bank: string[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const bank: string[] = JSON.parse(inputValues[0]);
	return numberOfBeams(bank);
}
