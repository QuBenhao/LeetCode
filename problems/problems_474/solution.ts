function findMaxForm(strs: string[], m: number, n: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const strs: string[] = JSON.parse(inputValues[0]);
	const m: number = JSON.parse(inputValues[1]);
	const n: number = JSON.parse(inputValues[2]);
	return findMaxForm(strs, m, n);
}
