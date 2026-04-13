function minimumTotalDistance(robot: number[], factory: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const robot: number[] = JSON.parse(inputValues[0]);
	const factory: number[][] = JSON.parse(inputValues[1]);
	return minimumTotalDistance(robot, factory);
}
