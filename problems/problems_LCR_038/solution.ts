function dailyTemperatures(temperatures: number[]): number[] {
	const n: number = temperatures.length;
	const ans: number[] = new Array(n).fill(0);
	const stack: number[] = [];
	for (let i: number = 0; i < n; i++) {
		while (stack.length > 0 && temperatures[i] > temperatures[stack[stack.length - 1]]) {
			const top: number = stack.pop();
			ans[top] = i - top;
		}
		stack.push(i);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const temperatures: number[] = JSON.parse(inputValues[0]);
	return dailyTemperatures(temperatures);
}
