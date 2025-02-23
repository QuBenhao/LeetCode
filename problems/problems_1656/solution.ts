class OrderedStream {
    constructor(n: number) {
        
    }

    insert(idKey: number, value: string): string[] {
        
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: OrderedStream = new OrderedStream(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "insert") {
			ans.push(obj.insert(opValues[i][0], opValues[i][1]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
