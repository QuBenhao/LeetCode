function minSpeedOnTime(dist: number[], hour: number): number {
	const n = dist.length;
	if (hour <= n - 1) return -1;
	let l = 1,
		r = 1e7;
	while (l < r) {
		const mid = (l + r) >> 1;
		let sum = 0;
		for (let i = 0; i < n - 1; i++) {
			sum += Math.ceil(dist[i] / mid);
		}
		sum += dist[n - 1] / mid;
		if (sum > hour) l = mid + 1;
		else r = mid;
	}
	return l;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const dist: number[] = JSON.parse(inputValues[0]);
	const hour: number = JSON.parse(inputValues[1]);
	return minSpeedOnTime(dist, hour);
}
