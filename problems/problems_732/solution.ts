class MyCalendarThree {
    constructor() {
        
    }

    book(startTime: number, endTime: number): number {
        
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * var obj = new MyCalendarThree()
 * var param_1 = obj.book(startTime,endTime)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: MyCalendarThree = new MyCalendarThree();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "book") {
			ans.push(obj.book(opValues[i][0], opValues[i][1]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
