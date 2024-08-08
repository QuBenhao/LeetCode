function generateParenthesis(n: number): string[] {
    const ans: Array<string> = [];
	const backtrack: Function = (s: string, left: number, right: number) => {
		if (left === n && right === n) {
			ans.push(s);
			return;
		}
		if (left < n) {
			backtrack(s + "(", left + 1, right);
		}
		if (right < left) {
			backtrack(s + ")", left, right + 1);
		}
	}
	backtrack("", 0, 0);
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return generateParenthesis(n);
}
