import {MinPriorityQueue} from "@datastructures-js/priority-queue";

function minimumTime(n: number, edges: number[][], disappear: number[]): number[] {
    const graph: number[][][] = Array.from({ length: n }, () => []);
	for (const [u, v, w] of edges) {
		graph[u].push([v, w]);
		graph[v].push([u, w]);
	}
	const dis: number[] = Array(n).fill(-1);
	dis[0] = 0;
	//@ts-ignore
	const pq: MinPriorityQueue<number[]> = new MinPriorityQueue<number[]>();
	pq.enqueue([0, 0], 0);
	while (!pq.isEmpty()) {
		const [d, u] = pq.dequeue().element;
		if (dis[u] < d) {
			continue;
		}
		for (const [v, w] of graph[u]) {
			const nd: number = d + w;
			if (nd < disappear[v] && (dis[v] === -1 || dis[v] > nd)) {
				dis[v] = nd;
				pq.enqueue([dis[v], v], dis[v]);
			}
		}
	}
	return dis;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	const disappear: number[] = JSON.parse(inputValues[2]);
	return minimumTime(n, edges, disappear);
}
