function detectCapitalUse(word: string): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const word: string = JSON.parse(splits[0]);
	return detectCapitalUse(word);
}
