import MinPriorityQueue from "@datastructures-js/priority-queue";


class SeatManager {
	//@ts-ignore
	pq: MinPriorityQueue;
    constructor(n: number) {
		//@ts-ignore
		this.pq = new MinPriorityQueue();
		for (let i: number = 1; i <= n; i++) {
			this.pq.enqueue(i);
		}
    }

    reserve(): number {
		return this.pq.dequeue().element;
    }

    unreserve(seatNumber: number): void {
        this.pq.enqueue(seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * var obj = new SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: SeatManager = new SeatManager(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "reserve") {
			ans.push(obj.reserve());
			continue;
		}
		if (operators[i] == "unreserve") {
			obj.unreserve(opValues[i][0]);
			ans.push(null);
			continue;
		}
		ans.push(null);
	}
	return ans;
}
