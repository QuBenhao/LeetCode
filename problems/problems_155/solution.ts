class MinStack {
	data: number[];
	helper: number[];
    constructor() {
        this.data = [];
		this.helper = [];
    }

    push(val: number): void {
        this.data.push(val);
		if (this.helper.length > 0 && this.helper[this.helper.length - 1] < val) {
			this.helper.push(this.helper[this.helper.length - 1]);
		} else {
			this.helper.push(val);
		}
    }

    pop(): void {
        this.data.pop();
		this.helper.pop();
    }

    top(): number {
		return this.data[this.data.length - 1];
    }

    getMin(): number {
        return this.helper[this.helper.length - 1];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: MinStack = new MinStack();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "push") {
			obj.push(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "pop") {
			obj.pop();
			ans.push(null);
			continue;
		}
		if (operators[i] == "top") {
			ans.push(obj.top());
			continue;
		}
		if (operators[i] == "getMin") {
			ans.push(obj.getMin());
			continue;
		}
		ans.push(null);
	}
	return ans;
}
