class DoublyLinkedList {
	public key: number;
	public value: number;
	public prev: DoublyLinkedList;
	public next: DoublyLinkedList;
	constructor(key: number, value: number) {
		this.key = key;
		this.value = value;
		this.prev = null;
		this.next = null;
	}

	insert(next: DoublyLinkedList): void {
		next.next = this.next;
		if (this.next != null) {
			this.next.prev = next;
		}
		this.next = next;
		next.prev = this;
	}

	remove(): void {
		if (this.prev != null) {
			this.prev.next = this.next;
		}
		if (this.next != null) {
			this.next.prev = this.prev;
		}
	}
}

class LRUCache {
	private capacity: number;
	private cache: Map<number, DoublyLinkedList>;
	private head: DoublyLinkedList;
	private tail: DoublyLinkedList;
    constructor(capacity: number) {
		this.capacity = capacity;
		this.cache = new Map<number, DoublyLinkedList>();
		this.head = new DoublyLinkedList(-1, -1);
		this.tail = new DoublyLinkedList(-1, -1);
		this.head.next = this.tail;
		this.tail.prev = this.head;
    }

    get(key: number): number {
		if (!this.cache.has(key)) {
			return -1;
		}
		const node: DoublyLinkedList = this.cache.get(key);
		node.remove();
		this.head.insert(node);
		return node.value;
    }

    put(key: number, value: number): void {
		let node: DoublyLinkedList;
		if (this.cache.has(key)) {
			node = this.cache.get(key);
			node.remove();
			node.value = value;
		} else {
			if (this.cache.size == this.capacity) {
				const last: DoublyLinkedList = this.tail.prev;
				last.remove();
				this.cache.delete(last.key);
			}
			node = new DoublyLinkedList(key, value);
			this.cache.set(key, node);
		}
		this.head.insert(node);
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
