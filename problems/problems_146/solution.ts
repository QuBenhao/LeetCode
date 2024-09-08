class DLinkedNode {
	key: number;
	value: number;
	prev: DLinkedNode | null;
	next: DLinkedNode | null;

	constructor(key: number = 0, value: number = 0) {
		this.key = key;
		this.value = value;
		this.prev = null;
		this.next = null;
	}
}

class LRUCache {
	private cache: Map<number, DLinkedNode>;
	private capacity: number;
	private head: DLinkedNode;
	private tail: DLinkedNode;

	private removeNode(node: DLinkedNode): void {
		if (node.prev != null) {
			node.prev.next = node.next;
		}
		if (node.next != null) {
			node.next.prev = node.prev;
		}
	}

	private addToHead(node: DLinkedNode): void {
		node.prev = this.head;
		node.next = this.head.next;
		this.head.next.prev = node;
		this.head.next = node;
	}

    constructor(capacity: number) {
		this.cache = new Map<number, DLinkedNode>();
		this.capacity = capacity;
		this.head = new DLinkedNode();
		this.tail = new DLinkedNode();
		this.head.next = this.tail;
		this.tail.prev = this.head;
    }

    get(key: number): number {
		if (!this.cache.has(key)) {
			return -1;
		}
		const node: DLinkedNode = this.cache.get(key);
		this.removeNode(node);
		this.addToHead(node);
		return node.value;
    }

    put(key: number, value: number): void {
		if (this.cache.has(key)) {
			const node: DLinkedNode = this.cache.get(key);
			node.value = value;
			this.removeNode(node);
			this.addToHead(node);
			return;
		}
		if (this.cache.size == this.capacity) {
			const node: DLinkedNode = this.tail.prev;
			this.removeNode(node);
			this.cache.delete(node.key);
		}
		const newNode: DLinkedNode = new DLinkedNode(key, value);
		this.cache.set(key, newNode);
		this.addToHead(newNode);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: LRUCache = new LRUCache(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "get") {
			ans.push(obj.get(opValues[i][0]));
			continue;
		}
		if (operators[i] == "put") {
			obj.put(opValues[i][0], opValues[i][1]);
			ans.push(null);
			continue;
		}
		ans.push(null);
	}
	return ans;
}
