function countKConstraintSubstrings(s: string, k: number, queries: number[][]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const queries: number[][] = JSON.parse(inputValues[2]);
	return countKConstraintSubstrings(s, k, queries);
}
