class WordsFrequency {
    constructor(book: string[]) {
        
    }

    get(word: string): number {
        
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * var obj = new WordsFrequency(book)
 * var param_1 = obj.get(word)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: WordsFrequency = new WordsFrequency(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "get") {
			ans.push(obj.get(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
