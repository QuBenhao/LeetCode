class RecentCounter {
	queue: Array<number>
    constructor() {
		this.queue = [];
    }

    ping(t: number): number {
		while (this.queue.length > 0 && this.queue[0] < t - 3000) {
			this.queue.shift();
		}
		this.queue.push(t);
		return this.queue.length;
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
