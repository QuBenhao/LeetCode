class RecentCounter {
    constructor() {

    }

    ping(t: number): number {

    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: RecentCounter = new RecentCounter();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "ping") {
			ans.push(obj.ping(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
