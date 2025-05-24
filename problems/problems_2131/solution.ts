function longestPalindrome(words: string[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(inputValues[0]);
	return longestPalindrome(words);
}
