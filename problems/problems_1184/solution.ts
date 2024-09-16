function distanceBetweenBusStops(distance: number[], start: number, destination: number): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const distance: number[] = JSON.parse(inputValues[0]);
	const start: number = JSON.parse(inputValues[1]);
	const destination: number = JSON.parse(inputValues[2]);
	return distanceBetweenBusStops(distance, start, destination);
}
