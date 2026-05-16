function canReach(arr: number[], start: number): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const arr: number[] = JSON.parse(inputValues[0]);
	const start: number = JSON.parse(inputValues[1]);
	return canReach(arr, start);
}
