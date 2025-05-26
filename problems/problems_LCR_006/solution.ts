function twoSum(numbers: number[], target: number): number[] {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const numbers: number[] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return twoSum(numbers, target);
}
