function minimumLengthEncoding(words: string[]): number {
	const n: number = words.length;
	const reversedWords: string[] = words.map((word: string) => word.split("").reverse().join(""));
	reversedWords.sort();
	let ans: number = 0;
	for (let i: number = 0; i < n - 1; i++) {
		if (reversedWords[i + 1].startsWith(reversedWords[i])) {
			continue;
		}
		ans += reversedWords[i].length + 1;
	}
	ans += reversedWords[n - 1].length + 1;
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(inputValues[0]);
	return minimumLengthEncoding(words);
}
