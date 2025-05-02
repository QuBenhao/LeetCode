function minDominoRotations(tops: number[], bottoms: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const tops: number[] = JSON.parse(inputValues[0]);
	const bottoms: number[] = JSON.parse(inputValues[1]);
	return minDominoRotations(tops, bottoms);
}
