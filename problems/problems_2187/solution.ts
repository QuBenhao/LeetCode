function minimumTime(time: number[], totalTrips: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const time: number[] = JSON.parse(inputValues[0]);
	const totalTrips: number = JSON.parse(inputValues[1]);
	return minimumTime(time, totalTrips);
}
