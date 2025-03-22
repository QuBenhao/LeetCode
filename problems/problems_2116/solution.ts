function canBeValid(s: string, locked: string): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const locked: string = JSON.parse(inputValues[1]);
	return canBeValid(s, locked);
}
