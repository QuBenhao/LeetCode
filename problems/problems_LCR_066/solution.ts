class MapSum {
    constructor() {

    }

    insert(key: string, val: number): void {

    }

    sum(prefix: string): number {

    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * var obj = new MapSum()
 * obj.insert(key,val)
 * var param_2 = obj.sum(prefix)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: MapSum = new MapSum();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "insert") {
			obj.insert(opValues[i][0], opValues[i][1]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "sum") {
			ans.push(obj.sum(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
