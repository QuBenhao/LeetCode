function largestRectangleArea(heights: number[]): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const heights: number[] = JSON.parse(inputValues[0]);
	return largestRectangleArea(heights);
}
