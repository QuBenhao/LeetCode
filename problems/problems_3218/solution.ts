function minimumCost(m: number, n: number, horizontalCut: number[], verticalCut: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const m: number = JSON.parse(inputValues[0]);
	const n: number = JSON.parse(inputValues[1]);
	const horizontalCut: number[] = JSON.parse(inputValues[2]);
	const verticalCut: number[] = JSON.parse(inputValues[3]);
	return minimumCost(m, n, horizontalCut, verticalCut);
}
