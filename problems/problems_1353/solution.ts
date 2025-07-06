function maxEvents(events: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const events: number[][] = JSON.parse(inputValues[0]);
	return maxEvents(events);
}
