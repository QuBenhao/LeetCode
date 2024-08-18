class MinHeap<T> {
    private heap: T[];

    constructor() {
        this.heap = [];
    }

    enqueue(element: T): void {
        this.heap.push(element);
        this.heapifyUp();
    }

    dequeue(): T | undefined {
        if (this.size() === 0) return undefined;
        if (this.size() === 1) return this.heap.pop();

        const root = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return root;
    }

    front(): T | undefined {
        return this.heap[0];
    }

    size(): number {
        return this.heap.length;
    }

    private heapifyUp(): void {
        let index = this.heap.length - 1;
        while (this.hasParent(index) && this.parent(index) > this.heap[index]) {
            this.swap(this.getParentIndex(index), index);
            index = this.getParentIndex(index);
        }
    }

    private heapifyDown(): void {
        let index = 0;
        while (this.hasLeftChild(index)) {
            let smallerChildIndex = this.getLeftChildIndex(index);
            if (this.hasRightChild(index) && this.rightChild(index) < this.leftChild(index)) {
                smallerChildIndex = this.getRightChildIndex(index);
            }

            if (this.heap[index] < this.heap[smallerChildIndex]) {
                break;
            } else {
                this.swap(index, smallerChildIndex);
            }
            index = smallerChildIndex;
        }
    }

    private getLeftChildIndex(parentIndex: number): number {
        return 2 * parentIndex + 1;
    }

    private getRightChildIndex(parentIndex: number): number {
        return 2 * parentIndex + 2;
    }

    private getParentIndex(childIndex: number): number {
        return Math.floor((childIndex - 1) / 2);
    }

    private hasLeftChild(index: number): boolean {
        return this.getLeftChildIndex(index) < this.heap.length;
    }

    private hasRightChild(index: number): boolean {
        return this.getRightChildIndex(index) < this.heap.length;
    }

    private hasParent(index: number): boolean {
        return this.getParentIndex(index) >= 0;
    }

    private leftChild(index: number): T {
        return this.heap[this.getLeftChildIndex(index)];
    }

    private rightChild(index: number): T {
        return this.heap[this.getRightChildIndex(index)];
    }

    private parent(index: number): T {
        return this.heap[this.getParentIndex(index)];
    }

    private swap(indexOne: number, indexTwo: number): void {
        const temp = this.heap[indexOne];
        this.heap[indexOne] = this.heap[indexTwo];
        this.heap[indexTwo] = temp;
    }
}


class KthLargest {
	k: number;
	pq: MinHeap<number>
    constructor(k: number, nums: number[]) {
		this.k = k;
		this.pq = new MinHeap<number>();
		for (const num of nums) {
			this.pq.enqueue(num);
			if (this.pq.size() > k) {
				this.pq.dequeue();
			}
		}
    }

    add(val: number): number {
		this.pq.enqueue(val);
		if (this.pq.size() > this.k) {
			this.pq.dequeue();
		}
		return this.pq.front();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: KthLargest = new KthLargest(opValues[0][0], opValues[0][1]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "add") {
			ans.push(obj.add(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
