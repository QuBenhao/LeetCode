function maxRunTime(n: number, batteries: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const batteries: number[] = JSON.parse(inputValues[1]);
	return maxRunTime(n, batteries);
}
