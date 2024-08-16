function evalRPN(tokens: string[]): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const tokens: string[] = JSON.parse(inputValues[0]);
	return evalRPN(tokens);
}
