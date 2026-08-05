function smallestNumber(n: number, t: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const t: number = JSON.parse(inputValues[1]);
	return smallestNumber(n, t);
}
