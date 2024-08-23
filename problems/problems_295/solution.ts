class MedianFinder {
    maxHeap: Heap
    minHeap: Heap
    constructor() {
        // 大顶堆 放小的那一半数字
        this.maxHeap = new Heap((a, b) => a > b);
        // 小顶堆 放大的那一半数字
        this.minHeap = new Heap((a, b) => a < b);
    }
    addNum(num: number): void {
        if (!this.maxHeap.size || num < this.maxHeap.peek()) {
            this.maxHeap.push(num);
        } else {
            this.minHeap.push(num);
        }
        // 维护两个堆的平衡
        if (this.maxHeap.size - this.minHeap.size > 1) {
            this.minHeap.push(this.maxHeap.pop());
        } else if (this.minHeap.size > this.maxHeap.size) {
            this.maxHeap.push(this.minHeap.pop());
        }
    }
    findMedian(): number {
        if ((this.maxHeap.size + this.minHeap.size) % 2 === 0) {
            return (this.maxHeap.peek() + this.minHeap.peek()) / 2;
        }
        return this.maxHeap.peek();
    }
}

class Heap {
    arr: Array<number>
    compare: Function
    constructor(compare) {
        this.arr = [0]; // 忽略 0 这个索引,方便计算左右节点
        this.compare = compare ? compare : (a, b) => a > b; // 默认是大顶堆
    }
    get size() {
        return this.arr.length - 1;
    }
    // 新增元素
    push(item) {
        this.arr.push(item);
        this.shiftUp(this.arr.length - 1);
    }
    // 元素上浮，k 是索引
    shiftUp(k) {
        let { arr, compare, parent } = this;
        // 当前元素 > 父元素，则进行交换
        while (k > 1 && compare(arr[k], arr[parent(k)])) {
            this.swap(parent(k), k);
            k = parent(k); // 更新 k 的位置为父元素的位置（交换了位置）
        }
    }
    // 弹出堆顶
    pop() {
        if (this.arr.length == 1) return null;
        this.swap(1, this.arr.length - 1);// 将结尾元素和堆顶元素交换位置
        let head = this.arr.pop(); // 删除堆顶
        this.sinkDown(1); // 再做下沉操作
        return head;
    }
    // 元素下沉
    sinkDown(k) {
        let { arr, compare, left, right, size } = this;
        while (left(k) <= size) {
            // 1. 拿到左右节点的最大值
            let child = left(k);
            if (right(k) <= size && compare(arr[right(k)], arr[child])) {
                child = right(k);
            }
            // 2. k 满足大顶堆或小顶堆，什么都不做
            if (compare(arr[k], arr[child])) {
                return;
            }
            // 3. 交换位置后，继续下沉操作
            this.swap(k, child);
            k = child; // 更新位置
        }
    }
    // 获取堆顶元素
    peek() {
        return this.arr[1];
    }
    // 获取左边元素节点
    left(k) {
        return k * 2;
    }
    // 获取右边元素节点
    right(k) {
        return k * 2 + 1;
    }
    // 获取父节点
    parent(k) {
        return Math.floor(k >> 1);
    }
    // i、j 交换位置
    swap(i, j) {
        [this.arr[i], this.arr[j]] = [this.arr[j], this.arr[i]];
    }
}

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
