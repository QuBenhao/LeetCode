function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const equations: string[][] = JSON.parse(inputValues[0]);
	const values: number[] = JSON.parse(inputValues[1]);
	const queries: string[][] = JSON.parse(inputValues[2]);
	return calcEquation(equations, values, queries);
}
