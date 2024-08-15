function dailyTemperatures(temperatures: number[]): number[] {
	const n: number = temperatures.length;
	const ans: Array<number> = new Array<number>(n).fill(0);
	const s: Array<number> = [];
	for (let i: number = 0; i < n; i++) {
		while (s.length > 0 && temperatures[s[s.length - 1]] < temperatures[i]) {
			const prev: number = s.pop()!!;
			ans[prev] = i - prev;
		}
		s.push(i);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const temperatures: number[] = JSON.parse(inputValues[0]);
	return dailyTemperatures(temperatures);
}
