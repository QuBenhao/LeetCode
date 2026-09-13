function isRectangleOverlap(rec1: number[], rec2: number[]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const rec1: number[] = JSON.parse(inputValues[0]);
	const rec2: number[] = JSON.parse(inputValues[1]);
	return isRectangleOverlap(rec1, rec2);
}
