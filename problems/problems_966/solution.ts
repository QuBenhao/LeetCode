function spellchecker(wordlist: string[], queries: string[]): string[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const wordlist: string[] = JSON.parse(inputValues[0]);
	const queries: string[] = JSON.parse(inputValues[1]);
	return spellchecker(wordlist, queries);
}
