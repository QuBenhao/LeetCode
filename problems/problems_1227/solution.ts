function nthPersonGetsNthSeat(n: number): number {
	return n === 1 ? 1 : 0.5;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return nthPersonGetsNthSeat(n);
}
