function minRectanglesToCoverPoints(points: number[][], w: number): number {
	points.sort((a, b) => a[0] - b[0]);
	const n: number = points.length;
	let ans: number = 0;
	for (let idx: number = 0; idx < n; ) {
		ans++;
		const cur: number = points[idx][0] + w;
		while (idx < n && points[idx][0] <= cur) {
			idx++;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const points: number[][] = JSON.parse(inputValues[0]);
	const w: number = JSON.parse(inputValues[1]);
	return minRectanglesToCoverPoints(points, w);
}
