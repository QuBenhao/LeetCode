function lenLongestFibSubseq(arr: number[]): number {
	const n: number = arr.length;
	const index: Map<number, number> = new Map<number, number>();
	for (let i: number = 0; i < n; i++) {
		index.set(arr[i], i);
	}
	let ans: number = 0;
	const dp: Map<number, Map<number, number>> = new Map<number, Map<number, number>>();
	for (let i: number = 0; i < n - 1; i++) {
		for (let j: number = i + 1; j < n; j++) {
			const nxt: number = arr[i] + arr[j];
			if (index.has(nxt)) {
				const k: number = index.get(nxt);
				if (!dp.has(j)) {
					dp.set(j, new Map<number, number>());
				}
				dp.get(j).set(k, (dp.has(i) && dp.get(i).has(j) ? dp.get(i).get(j) : 2) + 1);
				ans = Math.max(ans, dp.get(j).get(k));
			}
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const arr: number[] = JSON.parse(inputValues[0]);
	return lenLongestFibSubseq(arr);
}
