function confusingNumber(n: number): boolean {
	const trans: Map<number, number> = new Map([[0, 0], [1, 1], [6, 9], [8, 8], [9, 6]]);
	let revert: number = 0;
	for (let num: number = n; num > 0; num = Math.floor(num/10)) {
		const cur: number = num % 10;
		if (!trans.has(cur)) {
			return false;
		}
		revert = 10 * revert + trans.get(cur)!!;
	}
	return revert != n;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(splits[0]);
	return confusingNumber(n);
}
