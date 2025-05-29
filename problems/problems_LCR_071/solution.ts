class Solution {
    constructor(w: number[]) {

    }

    pickIndex(): number {

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(w)
 * var param_1 = obj.pickIndex()
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: Solution = new Solution(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "pickIndex") {
			ans.push(obj.pickIndex());
			continue;
		}
		ans.push(null);
	}
	return ans;
}
