function wordBreak(s: string, wordDict: string[]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const wordDict: string[] = JSON.parse(inputValues[1]);
	return wordBreak(s, wordDict);
}
