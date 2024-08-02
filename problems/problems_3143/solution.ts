function maxPointsInsideSquare(points: number[][], s: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const points: number[][] = JSON.parse(inputValues[0]);
	const s: string = JSON.parse(inputValues[1]);
	return maxPointsInsideSquare(points, s);
}
