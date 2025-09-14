function canBeTypedWords(text: string, brokenLetters: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const text: string = JSON.parse(inputValues[0]);
	const brokenLetters: string = JSON.parse(inputValues[1]);
	return canBeTypedWords(text, brokenLetters);
}
