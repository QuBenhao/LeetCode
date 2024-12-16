function minValidStrings(words: string[], target: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(inputValues[0]);
	const target: string = JSON.parse(inputValues[1]);
	return minValidStrings(words, target);
}
