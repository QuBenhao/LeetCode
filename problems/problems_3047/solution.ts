function largestSquareArea(bottomLeft: number[][], topRight: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const bottomLeft: number[][] = JSON.parse(inputValues[0]);
	const topRight: number[][] = JSON.parse(inputValues[1]);
	return largestSquareArea(bottomLeft, topRight);
}
