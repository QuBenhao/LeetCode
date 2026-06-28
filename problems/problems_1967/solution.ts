function numOfStrings(patterns: string[], word: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const patterns: string[] = JSON.parse(inputValues[0]);
	const word: string = JSON.parse(inputValues[1]);
	return numOfStrings(patterns, word);
}
