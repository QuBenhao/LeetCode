function generateParenthesis(n: number): string[] {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return generateParenthesis(n);
}
