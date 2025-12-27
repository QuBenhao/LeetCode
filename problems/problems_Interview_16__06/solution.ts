function smallestDifference(a: number[], b: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const a: number[] = JSON.parse(inputValues[0]);
	const b: number[] = JSON.parse(inputValues[1]);
	return smallestDifference(a, b);
}
