function isValid(s: string): boolean {
	const stack: string[] = [];
	const left: string = "([{", right: string = ")]}";
	for (const c of s) {
		if (left.includes(c)) {
			stack.push(c);
		} else if (stack.length == 0 || left.indexOf(stack.pop()) != right.indexOf(c)) {
			return false;
		}
	}
	return stack.length == 0;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return isValid(s);
}
