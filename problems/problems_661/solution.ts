function imageSmoother(img: number[][]): number[][] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const img: number[][] = JSON.parse(inputValues[0]);
	return imageSmoother(img);
}
