function intersectionSizeTwo(intervals: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const intervals: number[][] = JSON.parse(inputValues[0]);
	return intersectionSizeTwo(intervals);
}
