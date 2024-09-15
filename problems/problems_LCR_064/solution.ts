class TrieNode {
	public children: TrieNode[];
	public isEndOfWord: boolean;
	constructor() {
		this.children = new Array(26);
		this.isEndOfWord = false;
	}

	query(s: string, index: number, change: boolean): boolean {
		if (index == s.length) {
			return change && this.isEndOfWord;
		}
		const c: number = s.charCodeAt(index) - "a".charCodeAt(0);
		if (this.children[c] != null) {
			if (this.children[c].query(s, index + 1, change)) {
				return true;
			}
		}
		if (!change) {
			for (let i: number = 0; i < 26; i++) {
				if (i == c) {
					continue;
				}
				if (this.children[i] != null && this.children[i].query(s, index + 1, true)) {
					return true;
				}
			}
		}
		return false;
	}
}
class MagicDictionary {
	private root: TrieNode;
    constructor() {
		this.root = new TrieNode();
    }

    buildDict(dictionary: string[]): void {
		for (const word of dictionary) {
			let node: TrieNode = this.root;
			for (const c of word) {
				const index: number = c.charCodeAt(0) - "a".charCodeAt(0);
				if (node.children[index] == null) {
					node.children[index] = new TrieNode();
				}
				node = node.children[index];
			}
			node.isEndOfWord = true;
		}
    }

    search(searchWord: string): boolean {
		return this.root.query(searchWord, 0, false);
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
