function rowAndMaximumOnes(mat: number[][]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const mat: number[][] = JSON.parse(inputValues[0]);
	return rowAndMaximumOnes(mat);
}
