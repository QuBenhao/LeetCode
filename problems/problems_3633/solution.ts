function earliestFinishTime(landStartTime: number[], landDuration: number[], waterStartTime: number[], waterDuration: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const landStartTime: number[] = JSON.parse(inputValues[0]);
	const landDuration: number[] = JSON.parse(inputValues[1]);
	const waterStartTime: number[] = JSON.parse(inputValues[2]);
	const waterDuration: number[] = JSON.parse(inputValues[3]);
	return earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration);
}
