function minFlipsMonoIncr(s: string): number {
	const n: number = s.length;
	let ans: number = n, ones: number = 0;
	for (let i: number = 0; i < n; i++) {
		ans = Math.min(ans, ones * 2 - i);
		ones += s[i] === "1" ? 1 : 0;
	}
	return Math.min(ans + n - ones, ones);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return minFlipsMonoIncr(s);
}
