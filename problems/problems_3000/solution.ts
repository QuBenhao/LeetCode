function areaOfMaxDiagonal(dimensions: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const dimensions: number[][] = JSON.parse(inputValues[0]);
	return areaOfMaxDiagonal(dimensions);
}
