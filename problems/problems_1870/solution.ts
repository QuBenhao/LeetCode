function minSpeedOnTime(dist: number[], hour: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const dist: number[] = JSON.parse(inputValues[0]);
	const hour: number = JSON.parse(inputValues[1]);
	return minSpeedOnTime(dist, hour);
}
