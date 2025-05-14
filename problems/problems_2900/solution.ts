function getLongestSubsequence(words: string[], groups: number[]): string[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(inputValues[0]);
	const groups: number[] = JSON.parse(inputValues[1]);
	return getLongestSubsequence(words, groups);
}
