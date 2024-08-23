import {MaxPriorityQueue, MinPriorityQueue} from "@datastructures-js/priority-queue";


class MedianFinder {
    left: MaxPriorityQueue<number>;
    right: MinPriorityQueue<number>;

    constructor() {
        this.left = new MaxPriorityQueue();
        this.right = new MinPriorityQueue();
    }

    addNum(num: number): void {
        if (this.left.size() == this.right.size()) {
            if (this.right.isEmpty() || num <= this.right.front().element) {
                this.left.enqueue(num);
            } else {
                this.left.enqueue(this.right.dequeue().element);
                this.right.enqueue(num);
            }
        } else {
            if (num >= this.left.front().element) {
                this.right.enqueue(num);
            } else {
                this.right.enqueue(this.left.dequeue().element);
                this.left.enqueue(num);
            }
        }
    }

    findMedian(): number {
        return this.left.size() === this.right.size() ? (this.left.front().element + this.right.front().element) / 2 : this.left.front().element;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const operators: string[] = JSON.parse(inputValues[0]);
    const opValues: any[][] = JSON.parse(inputValues[1]);
    const ans: any[] = [null];
    const obj: MedianFinder = new MedianFinder();
    for (let i: number = 1; i < operators.length; i++) {
        if (operators[i] == "addNum") {
            obj.addNum(opValues[i][0]);
            ans.push(null);
            continue;
        }
        if (operators[i] == "findMedian") {
            ans.push(obj.findMedian());
            continue;
        }
        ans.push(null);
    }
    return ans;
}
