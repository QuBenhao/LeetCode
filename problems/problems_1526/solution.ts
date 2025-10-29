function minNumberOperations(target: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const target: number[] = JSON.parse(inputValues[0]);
	return minNumberOperations(target);
}
