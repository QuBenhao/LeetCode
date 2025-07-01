function kthGrammar(n: number, k: number): number {
    if (n == 1) {
		return 0;
	}
	return (1 - kthGrammar(n - 1, (k + 1) >> 1)) ^ (k & 1);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return kthGrammar(n, k);
}
