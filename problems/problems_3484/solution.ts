class Spreadsheet {
    constructor(rows: number) {
        
    }

    setCell(cell: string, value: number): void {
        
    }

    resetCell(cell: string): void {
        
    }

    getValue(formula: string): number {
        
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * var obj = new Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * var param_3 = obj.getValue(formula)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: Spreadsheet = new Spreadsheet(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "setCell") {
			obj.setCell(opValues[i][0], opValues[i][1]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "resetCell") {
			obj.resetCell(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "getValue") {
			ans.push(obj.getValue(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
