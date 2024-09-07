function maximumLength(nums: number[], k: number): number {
	const dp: Map<number, number[]> = new Map();
	const zd: number[] = Array(k + 1).fill(0);

	nums.forEach(v => {
			if (!dp.has(v)) {
					dp.set(v, Array(k + 1).fill(0));
			}
			const tmp = dp.get(v)!;
			for (let j = 0; j <= k; j++) {
					tmp[j]++;
					if (j > 0) {
							tmp[j] = Math.max(tmp[j], zd[j - 1] + 1);
					}
			}

			for (let j = 0; j <= k; j++) {
					zd[j] = Math.max(zd[j], tmp[j]);
					if (j > 0) {
							zd[j] = Math.max(zd[j], zd[j - 1]);
					}
			}
	});

	return zd[k];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return maximumLength(nums, k);
}
