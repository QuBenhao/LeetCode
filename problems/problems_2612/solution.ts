function minReverseOperations(n: number, p: number, banned: number[], k: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const p: number = JSON.parse(inputValues[1]);
	const banned: number[] = JSON.parse(inputValues[2]);
	const k: number = JSON.parse(inputValues[3]);
	return minReverseOperations(n, p, banned, k);
}
