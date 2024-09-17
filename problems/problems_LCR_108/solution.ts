function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const beginWord: string = JSON.parse(inputValues[0]);
	const endWord: string = JSON.parse(inputValues[1]);
	const wordList: string[] = JSON.parse(inputValues[2]);
	return ladderLength(beginWord, endWord, wordList);
}
