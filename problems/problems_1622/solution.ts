class Fancy {
    constructor() {
        
    }

    append(val: number): void {
        
    }

    addAll(inc: number): void {
        
    }

    multAll(m: number): void {
        
    }

    getIndex(idx: number): number {
        
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * var obj = new Fancy()
 * obj.append(val)
 * obj.addAll(inc)
 * obj.multAll(m)
 * var param_4 = obj.getIndex(idx)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: Fancy = new Fancy();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "append") {
			obj.append(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "addAll") {
			obj.addAll(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "multAll") {
			obj.multAll(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "getIndex") {
			ans.push(obj.getIndex(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
