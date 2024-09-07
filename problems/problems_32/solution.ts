function longestValidParentheses(s: string): number {
	const stack: number[] = [];
	let ans: number = 0;
	for (let i: number = 0; i < s.length; i++) {
		if (s[i] === "(") {
			stack.push(i);
		} else {
			if (stack.length > 0 && s[stack[stack.length - 1]] === "(") {
				stack.pop();
				ans = Math.max(ans, i - (stack.length > 0 ? stack[stack.length - 1] : -1));
			} else {
				stack.push(i);
			}
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return longestValidParentheses(s);
}
