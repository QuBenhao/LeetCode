function replaceWords(dictionary: string[], sentence: string): string {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const dictionary: string[] = JSON.parse(inputValues[0]);
	const sentence: string = JSON.parse(inputValues[1]);
	return replaceWords(dictionary, sentence);
}
