function numberOfPairs(points: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const points: number[][] = JSON.parse(inputValues[0]);
	return numberOfPairs(points);
}
