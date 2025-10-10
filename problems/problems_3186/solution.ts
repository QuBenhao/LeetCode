function maximumTotalDamage(power: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const power: number[] = JSON.parse(inputValues[0]);
	return maximumTotalDamage(power);
}
