function remainingMethods(n: number, k: number, invocations: number[][]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const invocations: number[][] = JSON.parse(inputValues[2]);
	return remainingMethods(n, k, invocations);
}
