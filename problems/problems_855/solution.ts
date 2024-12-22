class ExamRoom {
    constructor(n: number) {
        
    }

    seat(): number {
        
    }

    leave(p: number): void {
        
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * var obj = new ExamRoom(n)
 * var param_1 = obj.seat()
 * obj.leave(p)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: ExamRoom = new ExamRoom(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "seat") {
			ans.push(obj.seat());
			continue;
		}
		if (operators[i] == "leave") {
			obj.leave(opValues[i][0]);
			ans.push(null);
			continue;
		}
		ans.push(null);
	}
	return ans;
}
