class RangeFreqQuery {
    constructor(arr: number[]) {
        
    }

    query(left: number, right: number, value: number): number {
        
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * var obj = new RangeFreqQuery(arr)
 * var param_1 = obj.query(left,right,value)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: RangeFreqQuery = new RangeFreqQuery(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "query") {
			ans.push(obj.query(opValues[i][0], opValues[i][1], opValues[i][2]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
