function checkRecord(n: number): number {
	const mod: number = 1_000_000_007;
    let a: number = 1, al: number = 0, all: number = 0, p: number = 1, pl: number = 1, pll: number = 0;
	for (let i: number = 1; i <= n; i++) {
		[a, al, all, p, pl, pll] = [
			(a + al + all + p + pl + pll) % mod,
			a,
			al,
			(p + pl + pll) % mod,
			p,
			pl
		];
	}
	return a;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return checkRecord(n);
}
