function numberOfArrays(differences: number[], lower: number, upper: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const differences: number[] = JSON.parse(inputValues[0]);
	const lower: number = JSON.parse(inputValues[1]);
	const upper: number = JSON.parse(inputValues[2]);
	return numberOfArrays(differences, lower, upper);
}
