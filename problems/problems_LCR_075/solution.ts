function relativeSortArray(arr1: number[], arr2: number[]): number[] {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const arr1: number[] = JSON.parse(inputValues[0]);
	const arr2: number[] = JSON.parse(inputValues[1]);
	return relativeSortArray(arr1, arr2);
}
