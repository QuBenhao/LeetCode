function maximumRobots(chargeTimes: number[], runningCosts: number[], budget: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const chargeTimes: number[] = JSON.parse(inputValues[0]);
	const runningCosts: number[] = JSON.parse(inputValues[1]);
	const budget: number = JSON.parse(inputValues[2]);
	return maximumRobots(chargeTimes, runningCosts, budget);
}
