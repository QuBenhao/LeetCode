function countGoodTriplets(arr: number[], a: number, b: number, c: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const arr: number[] = JSON.parse(inputValues[0]);
	const a: number = JSON.parse(inputValues[1]);
	const b: number = JSON.parse(inputValues[2]);
	const c: number = JSON.parse(inputValues[3]);
	return countGoodTriplets(arr, a, b, c);
}
