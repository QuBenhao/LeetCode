function maxDistance(side: number, points: number[][], k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const side: number = JSON.parse(inputValues[0]);
	const points: number[][] = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return maxDistance(side, points, k);
}
