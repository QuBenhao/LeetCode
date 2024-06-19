function validWordSquare(words: string[]): boolean {

};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(splits[0]);
	return validWordSquare(words);
}
