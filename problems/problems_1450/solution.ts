function busyStudent(startTime: number[], endTime: number[], queryTime: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const startTime: number[] = JSON.parse(inputValues[0]);
	const endTime: number[] = JSON.parse(inputValues[1]);
	const queryTime: number = JSON.parse(inputValues[2]);
	return busyStudent(startTime, endTime, queryTime);
}
