function findSafeWalk(grid: number[][], health: number): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	const health: number = JSON.parse(inputValues[1]);
	return findSafeWalk(grid, health);
}
