function maxCount(m: number, n: number, ops: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const m: number = JSON.parse(inputValues[0]);
	const n: number = JSON.parse(inputValues[1]);
	const ops: number[][] = JSON.parse(inputValues[2]);
	return maxCount(m, n, ops);
}
