function canReachCorner(xCorner: number, yCorner: number, circles: number[][]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const xCorner: number = JSON.parse(inputValues[0]);
	const yCorner: number = JSON.parse(inputValues[1]);
	const circles: number[][] = JSON.parse(inputValues[2]);
	return canReachCorner(xCorner, yCorner, circles);
}
