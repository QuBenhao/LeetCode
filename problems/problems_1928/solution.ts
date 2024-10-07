function minCost(maxTime: number, edges: number[][], passingFees: number[]): number {
	const n = passingFees.length;
	const f: number[][] = Array.from({ length: maxTime + 1 }, () => Array(n).fill(Infinity));
	f[0][0] = passingFees[0];

	for (let t = 1; t <= maxTime; t++) {
			for (const [i, j, cost] of edges) {
					if (cost <= t) {
							if (f[t - cost][j] !== Infinity) {
									f[t][i] = Math.min(f[t][i], f[t - cost][j] + passingFees[i]);
							}
							if (f[t - cost][i] !== Infinity) {
									f[t][j] = Math.min(f[t][j], f[t - cost][i] + passingFees[j]);
							}
					}
			}
	}

	let ans = Infinity;
	for (let t = 1; t <= maxTime; t++) {
			ans = Math.min(ans, f[t][n - 1]);
	}
	return ans === Infinity ? -1 : ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const maxTime: number = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	const passingFees: number[] = JSON.parse(inputValues[2]);
	return minCost(maxTime, edges, passingFees);
}
