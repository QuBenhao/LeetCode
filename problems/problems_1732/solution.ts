function largestAltitude(gain: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const gain: number[] = JSON.parse(inputValues[0]);
	return largestAltitude(gain);
}
