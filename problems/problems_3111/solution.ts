function minRectanglesToCoverPoints(points: number[][], w: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const points: number[][] = JSON.parse(inputValues[0]);
	const w: number = JSON.parse(inputValues[1]);
	return minRectanglesToCoverPoints(points, w);
}
