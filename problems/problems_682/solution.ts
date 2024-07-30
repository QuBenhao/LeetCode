function calPoints(operations: string[]): number {
	let ans: number = 0;
	const stack: number[] = [];
	for (const op of operations) {
		if (op === "C") {
			ans -= stack.pop();
			continue;
		} else if (op === "D") {
			stack.push(stack[stack.length - 1] * 2);
		} else if (op === "+") {
			stack.push(stack[stack.length - 1] + stack[stack.length - 2]);
		} else {
			stack.push(parseInt(op));
		}
		ans += stack[stack.length - 1];
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operations: string[] = JSON.parse(inputValues[0]);
	return calPoints(operations);
}
