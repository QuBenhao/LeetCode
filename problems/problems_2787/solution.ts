function numberOfWays(n: number, x: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const x: number = JSON.parse(inputValues[1]);
	return numberOfWays(n, x);
}
