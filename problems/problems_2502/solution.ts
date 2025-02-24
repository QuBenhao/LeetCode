class Allocator {
    constructor(n: number) {
        
    }

    allocate(size: number, mID: number): number {
        
    }

    freeMemory(mID: number): number {
        
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * var obj = new Allocator(n)
 * var param_1 = obj.allocate(size,mID)
 * var param_2 = obj.freeMemory(mID)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: Allocator = new Allocator(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "allocate") {
			ans.push(obj.allocate(opValues[i][0], opValues[i][1]));
			continue;
		}
		if (operators[i] == "freeMemory") {
			ans.push(obj.freeMemory(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
