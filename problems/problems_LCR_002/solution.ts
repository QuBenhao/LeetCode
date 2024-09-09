function addBinary(a: string, b: string): string {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const a: string = JSON.parse(inputValues[0]);
	const b: string = JSON.parse(inputValues[1]);
	return addBinary(a, b);
}
