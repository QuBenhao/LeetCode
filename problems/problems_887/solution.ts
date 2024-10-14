function superEggDrop(k: number, n: number): number {
	const f: number[] = new Array(k + 1).fill(0);
	for (let i: number = 1; ; i++) {
		for (let j: number = k; j > 0; j--) {
			f[j] += f[j - 1] + 1;
		}
		if (f[k] >= n) {
			return i;
		}
	}
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const k: number = JSON.parse(inputValues[0]);
	const n: number = JSON.parse(inputValues[1]);
	return superEggDrop(k, n);
}
