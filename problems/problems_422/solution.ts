function validWordSquare(words: string[]): boolean {
	for (let i: number = 0; i < words.length; i++) {
		if (words[i].length > words.length) {
			return false;
		}
		for (let j: number = 0; j < i; j++) {
			if ((words[i].length <= j) != (words[j].length <= i)) {
				return false;
			} else if (words[i].length > j && words[i][j] != words[j][i]) {
				return false;
			}
		}
	}
	return true;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(splits[0]);
	return validWordSquare(words);
}
