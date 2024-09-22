function findJudge(n: number, trust: number[][]): number {
    const counter: number[] = new Array(n + 1).fill(0);
	for (const [a, b] of trust) {
		counter[a]--;
		counter[b]++;
	}
	for (let i = 1; i <= n; i++) {
		if (counter[i] === n - 1) {
			return i;
		}
	}
	return -1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const trust: number[][] = JSON.parse(inputValues[1]);
	return findJudge(n, trust);
}
