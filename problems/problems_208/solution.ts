class Trie {
	root: Map<string, any>;
    constructor() {
        this.root = new Map();
    }

    insert(word: string): void {
		let node: Map<string, any> = this.root;
		for (let i: number = 0; i < word.length; i++) {
			if (!node.has(word[i])) {
				node.set(word[i], new Map());
			}
			node = node.get(word[i]);
		}
		node.set("end", null);
    }

	private searchNode(word: string): Map<string, any> {
		let node: Map<string, any> = this.root;
		for (let i: number = 0; i < word.length; i++) {
			if (!node.has(word[i])) {
				return null;
			}
			node = node.get(word[i]);
		}
		return node;
	}

    search(word: string): boolean {
		const node: Map<string, any> = this.searchNode(word);
		return node != null && node.has("end");
    }

    startsWith(prefix: string): boolean {
        return this.searchNode(prefix) != null;
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
