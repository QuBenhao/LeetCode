function trapRainWater(heightMap: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const heightMap: number[][] = JSON.parse(inputValues[0]);
	return trapRainWater(heightMap);
}
