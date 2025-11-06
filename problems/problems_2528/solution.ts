function maxPower(stations: number[], r: number, k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const stations: number[] = JSON.parse(inputValues[0]);
	const r: number = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return maxPower(stations, r, k);
}
