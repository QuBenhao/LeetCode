function maxTaskAssign(tasks: number[], workers: number[], pills: number, strength: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const tasks: number[] = JSON.parse(inputValues[0]);
	const workers: number[] = JSON.parse(inputValues[1]);
	const pills: number = JSON.parse(inputValues[2]);
	const strength: number = JSON.parse(inputValues[3]);
	return maxTaskAssign(tasks, workers, pills, strength);
}
