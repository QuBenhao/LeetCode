function numSquares(n: number): number {
    const squares: Set<number> = new Set<number>();
	for (let i: number = 1; i * i <= n; i++) {
		squares.add(i * i);
	}
	const isDividedBy: Function = (n: number, count: number): boolean => {
		if (count === 1) {
			return squares.has(n);
		}
		// @ts-ignore
		for (const square of squares) {
			if (isDividedBy(n - square, count - 1)) {
				return true;
			}
		}
		return false;
	}
	for (let count: number = 1; count <= n; count++) {
		if (isDividedBy(n, count)) {
			return count;
		}
	}
	return n;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return numSquares(n);
}
