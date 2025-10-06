function avoidFlood(rains: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const rains: number[] = JSON.parse(inputValues[0]);
	return avoidFlood(rains);
}
