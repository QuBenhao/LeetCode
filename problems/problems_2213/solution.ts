function longestRepeating(s: string, queryCharacters: string, queryIndices: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const queryCharacters: string = JSON.parse(inputValues[1]);
	const queryIndices: number[] = JSON.parse(inputValues[2]);
	return longestRepeating(s, queryCharacters, queryIndices);
}
