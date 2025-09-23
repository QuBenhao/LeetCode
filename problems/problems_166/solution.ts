function fractionToDecimal(numerator: number, denominator: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const numerator: number = JSON.parse(inputValues[0]);
	const denominator: number = JSON.parse(inputValues[1]);
	return fractionToDecimal(numerator, denominator);
}
