function findMinDifference(timePoints: string[]): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const timePoints: string[] = JSON.parse(inputValues[0]);
	return findMinDifference(timePoints);
}
