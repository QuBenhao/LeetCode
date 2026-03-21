function findRotation(mat: number[][], target: number[][]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const mat: number[][] = JSON.parse(inputValues[0]);
	const target: number[][] = JSON.parse(inputValues[1]);
	return findRotation(mat, target);
}
