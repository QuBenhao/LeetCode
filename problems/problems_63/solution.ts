function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const obstacleGrid: number[][] = JSON.parse(inputValues[0]);
	return uniquePathsWithObstacles(obstacleGrid);
}
