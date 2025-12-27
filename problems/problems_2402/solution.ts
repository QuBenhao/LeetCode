function mostBooked(n: number, meetings: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const meetings: number[][] = JSON.parse(inputValues[1]);
	return mostBooked(n, meetings);
}
