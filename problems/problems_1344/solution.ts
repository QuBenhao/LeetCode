function angleClock(hour: number, minutes: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const hour: number = JSON.parse(inputValues[0]);
	const minutes: number = JSON.parse(inputValues[1]);
	return angleClock(hour, minutes);
}
