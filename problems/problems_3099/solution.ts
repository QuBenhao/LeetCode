function sumOfTheDigitsOfHarshadNumber(x: number): number {
    let s: number = 0;
	for (let num: number = x; num > 0; num = Math.floor(num / 10)) {
		s += num % 10;
	}
	return x % s == 0 ? s : -1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const x: number = JSON.parse(inputValues[0]);
	return sumOfTheDigitsOfHarshadNumber(x);
}
