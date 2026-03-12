function minNumberOfSeconds(mountainHeight: number, workerTimes: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const mountainHeight: number = JSON.parse(inputValues[0]);
	const workerTimes: number[] = JSON.parse(inputValues[1]);
	return minNumberOfSeconds(mountainHeight, workerTimes);
}
