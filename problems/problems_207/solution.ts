function canFinish(numCourses: number, prerequisites: number[][]): boolean {
	const degree: Array<number> = new Array<number>(numCourses).fill(0);
	const graph: Map<number, Array<number>> = new Map();
	for (const req of prerequisites) {
		degree[req[0]]++;
		if (!graph.has(req[1])) {
			graph.set(req[1], []);
		}
		graph.get(req[1])!!.push(req[0]);
	}
	const q: Array<number> = [];
	for (let i: number = 0; i < numCourses; i++) {
		if (degree[i] == 0) {
			q.push(i);
		}
	}
	let explored: number = 0;
	while (q.length > 0) {
		const cur: number = q.shift()!!;
		explored++;
		if (graph.has(cur)) {
			for (const other of graph.get(cur)!!) {
				degree[other]--;
				if (degree[other] == 0) {
					q.push(other);
				}
			}
		}
	}
	return explored == numCourses;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const numCourses: number = JSON.parse(inputValues[0]);
	const prerequisites: number[][] = JSON.parse(inputValues[1]);
	return canFinish(numCourses, prerequisites);
}
