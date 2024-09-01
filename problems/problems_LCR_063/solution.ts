class TrieNode {
	children: Map<string, TrieNode>;
	isEnd: boolean;
	constructor() {
		this.children = new Map();
		this.isEnd = false;
	}
}

function insert(root: TrieNode, word: string): void {
	let node: TrieNode = root;
	for (let i = 0; i < word.length; i++) {
		const ch: string = word[i];
		if (!node.children.has(ch)) {
			node.children.set(ch, new TrieNode());
		}
		node = node.children.get(ch) as TrieNode;
	}
	node.isEnd = true;
}

function searchPrefix(root: TrieNode, word: string): string {
	let node: TrieNode = root;
	let prefix: string = "";
	for (let i = 0; i < word.length; i++) {
		const ch: string = word[i];
		if (!node.children.has(ch)) {
			break;
		}
		prefix += ch;
		node = node.children.get(ch) as TrieNode;
		if (node.isEnd) {
			return prefix;
		}
	}
	return word;
}

function replaceWords(dictionary: string[], sentence: string): string {
	const root: TrieNode = new TrieNode();
	for (const word of dictionary) {
		insert(root, word);
	}
	const words: string[] = sentence.split(" ");
	for (let i = 0; i < words.length; i++) {
		words[i] = searchPrefix(root, words[i]);
	}
	return words.join(" ");
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const dictionary: string[] = JSON.parse(inputValues[0]);
	const sentence: string = JSON.parse(inputValues[1]);
	return replaceWords(dictionary, sentence);
}
