function successfulPairs(spells: number[], potions: number[], success: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const spells: number[] = JSON.parse(inputValues[0]);
	const potions: number[] = JSON.parse(inputValues[1]);
	const success: number = JSON.parse(inputValues[2]);
	return successfulPairs(spells, potions, success);
}
