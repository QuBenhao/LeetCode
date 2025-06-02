function maxCandies(status: number[], candies: number[], keys: number[][], containedBoxes: number[][], initialBoxes: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const status: number[] = JSON.parse(inputValues[0]);
	const candies: number[] = JSON.parse(inputValues[1]);
	const keys: number[][] = JSON.parse(inputValues[2]);
	const containedBoxes: number[][] = JSON.parse(inputValues[3]);
	const initialBoxes: number[] = JSON.parse(inputValues[4]);
	return maxCandies(status, candies, keys, containedBoxes, initialBoxes);
}
