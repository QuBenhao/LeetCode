function areSimilar(mat: number[][], k: number): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const mat: number[][] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return areSimilar(mat, k);
}
