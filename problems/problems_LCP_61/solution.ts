function temperatureTrend(temperatureA: number[], temperatureB: number[]): number {
	let ans: number = 0;
	for (let i: number = 1, cur: number = 0; i < temperatureA.length; i++) {
		const d1: number = temperatureA[i] - temperatureA[i - 1], d2: number = temperatureB[i] - temperatureB[i - 1];
		if (d1 * d2 > 0 || (d1 == 0 && d2 == 0)) {
			cur++;
			ans = Math.max(ans, cur);
		} else {
			cur = 0;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const temperatureA: number[] = JSON.parse(splits[0]);
	const temperatureB: number[] = JSON.parse(splits[1]);
	return temperatureTrend(temperatureA, temperatureB);
}
