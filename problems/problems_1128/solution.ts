function numEquivDominoPairs(dominoes: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const dominoes: number[][] = JSON.parse(inputValues[0]);
	return numEquivDominoPairs(dominoes);
}
