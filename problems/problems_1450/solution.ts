function busyStudent(startTime: number[], endTime: number[], queryTime: number): number {
    let ans: number = 0;
	for (let i = 0; i < startTime.length; i++) {
		if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
			ans++;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const startTime: number[] = JSON.parse(inputValues[0]);
	const endTime: number[] = JSON.parse(inputValues[1]);
	const queryTime: number = JSON.parse(inputValues[2]);
	return busyStudent(startTime, endTime, queryTime);
}
