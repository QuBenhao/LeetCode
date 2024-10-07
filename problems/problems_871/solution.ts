function minRefuelStops(target: number, startFuel: number, stations: number[][]): number {
	const n = stations.length;
	const dp = new Array(n + 1).fill(0);
	dp[0] = startFuel;
	for (let i = 0; i < n; i++) {
		for (let t = i; t >= 0; t--) {
			if (dp[t] >= stations[i][0]) {
				dp[t + 1] = Math.max(dp[t + 1], dp[t] + stations[i][1]);
			}
		}
	}
	for (let i = 0; i <= n; i++) {
		if (dp[i] >= target) {
			return i;
		}
	}
	return -1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const target: number = JSON.parse(inputValues[0]);
	const startFuel: number = JSON.parse(inputValues[1]);
	const stations: number[][] = JSON.parse(inputValues[2]);
	return minRefuelStops(target, startFuel, stations);
}
