function countPrimeSetBits(left: number, right: number): number {
	const primes: Set<number> = new Set([2, 3, 5, 7, 11, 13, 17, 19]);
	let count: number = 0;
	for (let i: number = left; i <= right; i++) {
		let bits: number = i;
		bits = (bits & 0x55555555) + ((bits >> 1) & 0x55555555);
		bits = (bits & 0x33333333) + ((bits >> 2) & 0x33333333);
		bits = (bits & 0x0f0f0f0f) + ((bits >> 4) & 0x0f0f0f0f);
		bits = (bits & 0x00ff00ff) + ((bits >> 8) & 0x00ff00ff);
		bits = (bits & 0x0000ffff) + ((bits >> 16) & 0x0000ffff);
		if (primes.has(bits)) {
			count++;
		}
	}
	return count;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const left: number = JSON.parse(inputValues[0]);
	const right: number = JSON.parse(inputValues[1]);
	return countPrimeSetBits(left, right);
}
