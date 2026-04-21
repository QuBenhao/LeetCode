function twoEditWords(queries: string[], dictionary: string[]): string[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const queries: string[] = JSON.parse(inputValues[0]);
	const dictionary: string[] = JSON.parse(inputValues[1]);
	return twoEditWords(queries, dictionary);
}
