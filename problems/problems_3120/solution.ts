function numberOfSpecialChars(word: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const word: string = JSON.parse(inputValues[0]);
	return numberOfSpecialChars(word);
}
