class MedianFinder {
    constructor() {
        
    }

    addNum(num: number): void {
        
    }

    findMedian(): number {
        
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
