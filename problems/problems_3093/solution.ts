function stringIndices(wordsContainer: string[], wordsQuery: string[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const wordsContainer: string[] = JSON.parse(inputValues[0]);
	const wordsQuery: string[] = JSON.parse(inputValues[1]);
	return stringIndices(wordsContainer, wordsQuery);
}
