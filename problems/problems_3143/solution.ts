function maxPointsInsideSquare(points: number[][], s: string): number {
	const idxMap: Array<number> = new Array<number>(26).fill(0x3f3f3f3f);
	let dist: number = 0x3f3f3f3f;
	for (let i: number = 0; i < points.length; i++) {
		const idx: number = s.charCodeAt(i) - "a".charCodeAt(0);
		const cur: number = Math.max(Math.abs(points[i][0]), Math.abs(points[i][1]));
		if (cur < idxMap[idx]) {
			dist = Math.min(dist, idxMap[idx]);
			idxMap[idx] = cur;
		} else {
			dist = Math.min(dist, cur);
		}
	}
	let ans: number = 0;
	for (let i: number = 0; i < 26; i++) {
		if (idxMap[i] < dist) {
			ans++;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const points: number[][] = JSON.parse(inputValues[0]);
	const s: string = JSON.parse(inputValues[1]);
	return maxPointsInsideSquare(points, s);
}
