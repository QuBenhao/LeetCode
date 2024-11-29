function isAlienSorted(words: string[], order: string): boolean {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(inputValues[0]);
	const order: string = JSON.parse(inputValues[1]);
	return isAlienSorted(words, order);
}
