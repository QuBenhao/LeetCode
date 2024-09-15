import {MaxPriorityQueue} from "@datastructures-js/priority-queue";

function topKFrequent(nums: number[], k: number): number[] {
	const counter: Map<number, number> = new Map<number, number>();
	for (const num of nums) {
		counter.set(num, (counter.get(num) || 0) + 1);
	}
	const pq = new MaxPriorityQueue();
	for (const [num, freq] of counter) {
		pq.enqueue(num, freq);
	}
	const ans: number[] = [];
	for (let i: number = 0; i < k; i++) {
		// @ts-ignore
		ans.push(pq.dequeue().element);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return topKFrequent(nums, k);
}
