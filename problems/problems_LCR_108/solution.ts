function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
	const wordSet: Set<string> = new Set(wordList);
	if (!wordSet.has(endWord)) {
		return 0;
	}
	const queue: string[] = [beginWord];
	let level: number = 1;
	while (queue.length > 0) {
		const n: number = queue.length;
		for (let i: number = 0; i < n; i++) {
			const word: string = queue.shift()!;
			if (word === endWord) {
				return level;
			}
			for (let j: number = 0; j < word.length; j++) {
				for (let k: number = 0; k < 26; k++) {
					const newWord: string = word.slice(0, j) + String.fromCharCode(97 + k) + word.slice(j + 1);
					if (wordSet.has(newWord)) {
						queue.push(newWord);
						wordSet.delete(newWord);
					}
				}
			}
		}
		level++;
	}
	return 0;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const beginWord: string = JSON.parse(inputValues[0]);
	const endWord: string = JSON.parse(inputValues[1]);
	const wordList: string[] = JSON.parse(inputValues[2]);
	return ladderLength(beginWord, endWord, wordList);
}
