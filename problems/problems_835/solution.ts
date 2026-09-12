function largestOverlap(img1: number[][], img2: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const img1: number[][] = JSON.parse(inputValues[0]);
	const img2: number[][] = JSON.parse(inputValues[1]);
	return largestOverlap(img1, img2);
}
