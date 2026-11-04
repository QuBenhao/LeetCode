function findTheDistanceValue(arr1: number[], arr2: number[], d: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const arr1: number[] = JSON.parse(inputValues[0]);
	const arr2: number[] = JSON.parse(inputValues[1]);
	const d: number = JSON.parse(inputValues[2]);
	return findTheDistanceValue(arr1, arr2, d);
}
