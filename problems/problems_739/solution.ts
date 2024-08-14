function dailyTemperatures(temperatures: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const temperatures: number[] = JSON.parse(inputValues[0]);
	return dailyTemperatures(temperatures);
}
