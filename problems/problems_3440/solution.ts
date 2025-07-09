function maxFreeTime(eventTime: number, startTime: number[], endTime: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const eventTime: number = JSON.parse(inputValues[0]);
	const startTime: number[] = JSON.parse(inputValues[1]);
	const endTime: number[] = JSON.parse(inputValues[2]);
	return maxFreeTime(eventTime, startTime, endTime);
}
