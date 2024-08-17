class KthLargest {
    constructor(k: number, nums: number[]) {

    }

    add(val: number): number {

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
