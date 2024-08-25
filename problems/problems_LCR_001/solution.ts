const INT_MAX = 2147483647, INT_MIN = -2147483648;

function divide(a: number, b: number): number {
	if (a == INT_MIN && b == -1) {
		return INT_MAX;
	}
	let dividend: number = Math.abs(a), divisor: number = Math.abs(b), ans: number = 0;
	for (let i: number = 31; i >= 0; i--) {
		if ((dividend >>> i) >= divisor) {
			if (i == 31) {
				dividend += INT_MIN;
				ans -= INT_MIN;
			} else {
				ans |= 1 << i;
				dividend -= divisor << i;
			}
		}
	}
	if (ans === 0) {
		return 0;
	}
	return (a > 0) === (b > 0) ? ans : -ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const a: number = JSON.parse(inputValues[0]);
	const b: number = JSON.parse(inputValues[1]);
	return divide(a, b);
}
