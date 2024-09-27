function countBits(n: number): number[] {
	const bits: number[] = Array(n + 1).fill(0);
	for (let i = 1; i <= n; ++i) {
		bits[i] = bits[i >> 1] + (i & 1);
	}
	return bits;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return countBits(n);
}
