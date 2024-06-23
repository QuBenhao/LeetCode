function detectCapitalUse(word: string): boolean {
    if (word.charAt(word.length - 1).toUpperCase() == word.charAt(word.length - 1)) {
		for (let i: number = 0; i < word.length - 1; i++) {
			if (word.charAt(i).toLowerCase() == word.charAt(i)) {
				return false;
			}
		}
	} else if (word.charAt(0).toUpperCase() == word.charAt(0)) {
		for (let i: number = 1; i < word.length - 1; i++) {
			if (word.charAt(i).toUpperCase() == word.charAt(i)) {
				return false;
			}
		}
	} else {
		for (let i: number = 1; i < word.length - 1; i++) {
			if (word.charAt(i).toUpperCase() == word.charAt(i)) {
				return false;
			}
		}
	}
	return true;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const word: string = JSON.parse(splits[0]);
	return detectCapitalUse(word);
}
