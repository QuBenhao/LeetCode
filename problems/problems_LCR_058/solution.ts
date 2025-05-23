class MyCalendar {
    constructor() {

    }

    book(start: number, end: number): boolean {

    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: MyCalendar = new MyCalendar();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "book") {
			ans.push(obj.book(opValues[i][0], opValues[i][1]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
