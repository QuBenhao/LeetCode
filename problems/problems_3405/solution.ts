function countGoodArrays(n: number, m: number, k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const m: number = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return countGoodArrays(n, m, k);
}
