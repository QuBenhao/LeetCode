function minimumEffort(tasks: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const tasks: number[][] = JSON.parse(inputValues[0]);
	return minimumEffort(tasks);
}
