function minimumHammingDistance(source: number[], target: number[], allowedSwaps: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const source: number[] = JSON.parse(inputValues[0]);
	const target: number[] = JSON.parse(inputValues[1]);
	const allowedSwaps: number[][] = JSON.parse(inputValues[2]);
	return minimumHammingDistance(source, target, allowedSwaps);
}
