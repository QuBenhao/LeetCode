class RandomizedSet {
    constructor() {

    }

    insert(val: number): boolean {

    }

    remove(val: number): boolean {

    }

    getRandom(): number {

    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: RandomizedSet = new RandomizedSet();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "insert") {
			ans.push(obj.insert(opValues[i][0]));
			continue;
		}
		if (operators[i] == "remove") {
			ans.push(obj.remove(opValues[i][0]));
			continue;
		}
		if (operators[i] == "getRandom") {
			ans.push(obj.getRandom());
			continue;
		}
		ans.push(null);
	}
	return ans;
}
