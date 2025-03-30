function percentageLetter(s: string, letter: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const letter: string = JSON.parse(inputValues[1]);
	return percentageLetter(s, letter);
}
