class Skiplist {
    constructor() {
        
    }

    search(target: number): boolean {
        
    }

    add(num: number): void {
        
    }

    erase(num: number): boolean {
        
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * var obj = new Skiplist()
 * var param_1 = obj.search(target)
 * obj.add(num)
 * var param_3 = obj.erase(num)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: Skiplist = new Skiplist();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "search") {
			ans.push(obj.search(opValues[i][0]));
			continue;
		}
		if (operators[i] == "add") {
			obj.add(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "erase") {
			ans.push(obj.erase(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
