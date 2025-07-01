function possibleStringCount(word: string, k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const word: string = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return possibleStringCount(word, k);
}
