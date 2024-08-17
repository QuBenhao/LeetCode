function evalRPN(tokens: string[]): number {
	const values: Array<number> = [];
	for (const token of tokens) {
		switch (token) {
			case "+":
				values.push(values.pop() + values.pop());
				break;
			case "-":
				values.push(-values.pop() + values.pop());
				break;
			case "*":
				values.push(values.pop() * values.pop());
				break;
			case "/":
				const divisor: number = values.pop();
				values.push(Math.trunc(values.pop() / divisor));
				break;
			default:
				values.push(parseInt(token));
		}
	}
	return values.pop();
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const tokens: string[] = JSON.parse(inputValues[0]);
	return evalRPN(tokens);
}
