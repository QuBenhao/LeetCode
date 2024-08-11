class MagicDictionary {
    constructor() {
        
    }

    buildDict(dictionary: string[]): void {
        
    }

    search(searchWord: string): boolean {
        
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = new MagicDictionary()
 * obj.buildDict(dictionary)
 * var param_2 = obj.search(searchWord)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: MagicDictionary = new MagicDictionary();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "buildDict") {
			obj.buildDict(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "search") {
			ans.push(obj.search(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
