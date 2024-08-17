function minimumOperationsToMakeKPeriodic(word: string, k: number): number {
	const n: number = word.length;
	const count: Map<string, number> = new Map();
	let ans: number = 0;
	for (let i = 0; i < n; i+=k) {
		const sub: string = word.substring(i, i + k);
		if (!count.has(sub)) {
			count.set(sub, 0);
		}
		count.set(sub, count.get(sub) + 1);
		ans = Math.max(ans, count.get(sub));
	}
	return Math.floor(n / k) - ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const word: string = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return minimumOperationsToMakeKPeriodic(word, k);
}
