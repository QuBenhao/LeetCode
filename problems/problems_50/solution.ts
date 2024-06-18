function myPow(x: number, n: number): number {
	if (x == 0.0) {
		return 0.0;
	}
	if (n < 0) {
		x = 1.0 / x;
		n = -n;
	}
	let ans: number = 1.0;
	while (n > 0) {
		if ((n & 1) == 1) {
			ans *= x;
		}
		x *= x;
		n >>= 1;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const x: number = JSON.parse(splits[0]);
	const n: number = JSON.parse(splits[1]);
	return myPow(x, n);
}
