function countCompleteDayPairs(hours: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const hours: number[] = JSON.parse(inputValues[0]);
	return countCompleteDayPairs(hours);
}
