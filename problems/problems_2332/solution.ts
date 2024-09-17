function latestTimeCatchTheBus(buses: number[], passengers: number[], capacity: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const buses: number[] = JSON.parse(inputValues[0]);
	const passengers: number[] = JSON.parse(inputValues[1]);
	const capacity: number = JSON.parse(inputValues[2]);
	return latestTimeCatchTheBus(buses, passengers, capacity);
}
