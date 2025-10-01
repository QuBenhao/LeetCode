function maxBottlesDrunk(numBottles: number, numExchange: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const numBottles: number = JSON.parse(inputValues[0]);
	const numExchange: number = JSON.parse(inputValues[1]);
	return maxBottlesDrunk(numBottles, numExchange);
}
