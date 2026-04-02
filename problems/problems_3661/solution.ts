function maxWalls(robots: number[], distance: number[], walls: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const robots: number[] = JSON.parse(inputValues[0]);
	const distance: number[] = JSON.parse(inputValues[1]);
	const walls: number[] = JSON.parse(inputValues[2]);
	return maxWalls(robots, distance, walls);
}
