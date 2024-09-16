function distanceBetweenBusStops(distance: number[], start: number, destination: number): number {
	const n: number = distance.length, min: number = Math.min(start, destination), max: number = Math.max(start, destination);
	let clockwise: number = 0, counterclockwise: number = 0;
	for (let i: number = 0; i < n; i++) {
		if (i >= min && i < max) {
			clockwise += distance[i];
		} else {
			counterclockwise += distance[i];
		}
	}
	return Math.min(clockwise, counterclockwise);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const distance: number[] = JSON.parse(inputValues[0]);
	const start: number = JSON.parse(inputValues[1]);
	const destination: number = JSON.parse(inputValues[2]);
	return distanceBetweenBusStops(distance, start, destination);
}
