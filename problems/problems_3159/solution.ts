function occurrencesOfElement(nums: number[], queries: number[], x: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const queries: number[] = JSON.parse(inputValues[1]);
	const x: number = JSON.parse(inputValues[2]);
	return occurrencesOfElement(nums, queries, x);
}
