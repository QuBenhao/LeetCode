function countPrefixes(words: string[], s: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(inputValues[0]);
	const s: string = JSON.parse(inputValues[1]);
	return countPrefixes(words, s);
}
