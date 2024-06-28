function paintWalls(cost: number[], time: number[]): number {
	const n: number = cost.length;
	const f: number[] = new Array(n + 1).fill(Number.MAX_SAFE_INTEGER / 2);
	f[0] = 0;
	for (let i = 0; i < n; i++) {
		const t: number = time[i] + 1;
		for (let j = n; j > 0; j--) {
			f[j] = Math.min(f[j], f[Math.max(0, j - t)] + cost[i]);
		}
	}
	return f[n];
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const cost: number[] = JSON.parse(splits[0]);
	const time: number[] = JSON.parse(splits[1]);
	return paintWalls(cost, time);
}
