function maxFreeTime(eventTime: number, k: number, startTime: number[], endTime: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const eventTime: number = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const startTime: number[] = JSON.parse(inputValues[2]);
	const endTime: number[] = JSON.parse(inputValues[3]);
	return maxFreeTime(eventTime, k, startTime, endTime);
}
