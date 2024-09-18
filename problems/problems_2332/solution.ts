function latestTimeCatchTheBus(buses: number[], passengers: number[], capacity: number): number {
    buses.sort((a, b) => a - b);
	passengers.sort((a, b) => a - b);
	const n: number = passengers.length;
	let j: number = 0, c: number = 0;
	for (const bus of buses) {
		c = capacity;
		while (c > 0 && j < n && passengers[j] <= bus) {
			c--;
			j++;
		}
	}
	j--;
	let ans: number = c > 0 ? buses[buses.length - 1] : passengers[j];
	while (j >= 0 && passengers[j] === ans) {
		j--;
		ans--;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const buses: number[] = JSON.parse(inputValues[0]);
	const passengers: number[] = JSON.parse(inputValues[1]);
	const capacity: number = JSON.parse(inputValues[2]);
	return latestTimeCatchTheBus(buses, passengers, capacity);
}
