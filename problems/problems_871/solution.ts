function minRefuelStops(target: number, startFuel: number, stations: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const target: number = JSON.parse(inputValues[0]);
	const startFuel: number = JSON.parse(inputValues[1]);
	const stations: number[][] = JSON.parse(inputValues[2]);
	return minRefuelStops(target, startFuel, stations);
}
