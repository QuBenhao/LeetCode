function mySqrt(x: number): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const x: number = JSON.parse(inputValues[0]);
	return mySqrt(x);
}
