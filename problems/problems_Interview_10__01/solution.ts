/**
 Do not return anything, modify A in-place instead.
 */
function merge(A: number[], m: number, B: number[], n: number): void {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const A: number[] = JSON.parse(inputValues[0]);
	const m: number = JSON.parse(inputValues[1]);
	const B: number[] = JSON.parse(inputValues[2]);
	const n: number = JSON.parse(inputValues[3]);
	merge(A, m, B, n)
	return A;
}
