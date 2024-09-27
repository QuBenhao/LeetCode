class BookMyShow {
    constructor(n: number, m: number) {
        
    }

    gather(k: number, maxRow: number): number[] {
        
    }

    scatter(k: number, maxRow: number): boolean {
        
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * var obj = new BookMyShow(n, m)
 * var param_1 = obj.gather(k,maxRow)
 * var param_2 = obj.scatter(k,maxRow)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: BookMyShow = new BookMyShow(opValues[0][0], opValues[0][1]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "gather") {
			ans.push(obj.gather(opValues[i][0], opValues[i][1]));
			continue;
		}
		if (operators[i] == "scatter") {
			ans.push(obj.scatter(opValues[i][0], opValues[i][1]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
