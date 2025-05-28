class MovingAverage {
    constructor(size: number) {

    }

    next(val: number): number {

    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: MovingAverage = new MovingAverage(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "next") {
			ans.push(obj.next(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
