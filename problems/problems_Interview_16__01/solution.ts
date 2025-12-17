function swapNumbers(numbers: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const numbers: number[] = JSON.parse(inputValues[0]);
	return swapNumbers(numbers);
}
