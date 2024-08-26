class Trie {
    constructor() {
        
    }

    insert(word: string): void {
        
    }

    search(word: string): boolean {
        
    }

    startsWith(prefix: string): boolean {
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: Trie = new Trie();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "insert") {
			obj.insert(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "search") {
			ans.push(obj.search(opValues[i][0]));
			continue;
		}
		if (operators[i] == "startsWith") {
			ans.push(obj.startsWith(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
