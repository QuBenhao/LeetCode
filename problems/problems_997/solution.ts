function findJudge(n: number, trust: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const trust: number[][] = JSON.parse(inputValues[1]);
	return findJudge(n, trust);
}
