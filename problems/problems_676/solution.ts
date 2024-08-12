class TrieNode {
	public children: Map<string, TrieNode>;
	public isEnd: boolean;
	constructor() {
		this.children = new Map<string, TrieNode>();
		this.isEnd = false;
	}
	insert(word: string): void {
		let node: TrieNode = this;
		for (let i: number = 0; i < word.length; i++) {
			const ch: string = word[i];
			if (!node.children.has(ch)) {
				node.children.set(ch, new TrieNode());
			}
			node = node.children.get(ch);
		}
		node.isEnd = true;
	}
}

class MagicDictionary {
	private root: TrieNode;
    constructor() {
        this.root = new TrieNode();
    }

    buildDict(dictionary: string[]): void {
        for (const word of dictionary) {
			this.root.insert(word);
		}
    }

    search(searchWord: string): boolean {
        const query: Function = (node: TrieNode, index: number, remain: number): boolean => {
			if (index == searchWord.length) {
				return node.isEnd && remain == 0;
			}
			if (node.children.has(searchWord[index])) {
				if (query(node.children.get(searchWord[index]), index + 1, remain)) {
					return true;
				}
			}
			if (remain-- == 0) {
				return false;
			}
			// @ts-ignore
			for (const [k, v] of node.children.entries()) {
				if (k === searchWord[index]) {
					continue;
				}
				if (query(v, index + 1, remain)) {
					return true;
				}
			}
			return false;
		}
		return query(this.root, 0, 1);
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
