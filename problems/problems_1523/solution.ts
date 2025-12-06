function countOdds(low: number, high: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const low: number = JSON.parse(inputValues[0]);
	const high: number = JSON.parse(inputValues[1]);
	return countOdds(low, high);
}
