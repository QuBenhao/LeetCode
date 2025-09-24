function minimumTotal(triangle: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const triangle: number[][] = JSON.parse(inputValues[0]);
	return minimumTotal(triangle);
}
