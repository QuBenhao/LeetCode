function temperatureTrend(temperatureA: number[], temperatureB: number[]): number {

};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const temperatureA: number[] = JSON.parse(splits[0]);
	const temperatureB: number[] = JSON.parse(splits[1]);
	return temperatureTrend(temperatureA, temperatureB);
}
