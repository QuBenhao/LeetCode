function searchMatrix(matrix: number[][], target: number): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const matrix: number[][] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return searchMatrix(matrix, target);
}
