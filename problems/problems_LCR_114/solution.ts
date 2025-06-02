function alienOrder(words: string[]): string {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(inputValues[0]);
	return alienOrder(words);
}
