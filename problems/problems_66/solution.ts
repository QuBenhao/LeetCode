function plusOne(digits: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const digits: number[] = JSON.parse(inputValues[0]);
	return plusOne(digits);
}
