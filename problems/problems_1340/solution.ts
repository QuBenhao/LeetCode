function maxJumps(arr: number[], d: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const arr: number[] = JSON.parse(inputValues[0]);
	const d: number = JSON.parse(inputValues[1]);
	return maxJumps(arr, d);
}
