function minimumOperations(num: string): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const num: string = JSON.parse(inputValues[0]);
	return minimumOperations(num);
}
