class NumberContainers {
    constructor() {
        
    }

    change(index: number, number: number): void {
        
    }

    find(number: number): number {
        
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * var obj = new NumberContainers()
 * obj.change(index,number)
 * var param_2 = obj.find(number)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: NumberContainers = new NumberContainers();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "change") {
			obj.change(opValues[i][0], opValues[i][1]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "find") {
			ans.push(obj.find(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
