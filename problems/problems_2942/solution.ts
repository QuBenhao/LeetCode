function findWordsContaining(words: string[], x: string): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(inputValues[0]);
	const x: string = JSON.parse(inputValues[1]);
	return findWordsContaining(words, x);
}
