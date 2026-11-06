function assignTasks(servers: number[], tasks: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const servers: number[] = JSON.parse(inputValues[0]);
	const tasks: number[] = JSON.parse(inputValues[1]);
	return assignTasks(servers, tasks);
}
