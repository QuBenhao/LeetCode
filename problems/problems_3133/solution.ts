function minEnd(n: number, x: number): number {
	n--;
	let res: bigint = BigInt(x);
	for (let i: number = 0, j: number = 0; n >> j > 0; i++) {
		if (((res >> BigInt(i)) & 1n) === 0n) {
			res |= ((BigInt(n) >> BigInt(j)) & 1n) << BigInt(i);
			j++;
		}
	}
	return Number(res);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const x: number = JSON.parse(inputValues[1]);
	return minEnd(n, x);
}
