function numSimilarGroups(strs: string[]): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const strs: string[] = JSON.parse(inputValues[0]);
	return numSimilarGroups(strs);
}
