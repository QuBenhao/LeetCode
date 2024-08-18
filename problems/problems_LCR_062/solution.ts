class Trie {
	children: Map<string, Trie>
	isEnd: boolean
    constructor() {
		this.children = new Map<string, Trie>();
		this.isEnd = false;
    }

    insert(word: string): void {
		let node: Trie = this;
		for (const ch of word) {
			if (!node.children.has(ch)) {
				node.children.set(ch, new Trie());
			}
			node = node.children.get(ch);
		}
		node.isEnd = true;
    }

	searchPrefix(prefix: string): Trie {
		let node: Trie = this;
		for (const ch of prefix) {
			if (!node.children.has(ch)) {
				return null;
			}
			node = node.children.get(ch);
		}
		return node;
	}

    search(word: string): boolean {
		const node: Trie = this.searchPrefix(word);
		return node != null && node.isEnd;
    }

    startsWith(prefix: string): boolean {
		return this.searchPrefix(prefix) != null;
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
