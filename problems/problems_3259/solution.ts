function maxEnergyBoost(energyDrinkA: number[], energyDrinkB: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const energyDrinkA: number[] = JSON.parse(inputValues[0]);
	const energyDrinkB: number[] = JSON.parse(inputValues[1]);
	return maxEnergyBoost(energyDrinkA, energyDrinkB);
}
