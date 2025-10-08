function minTime(skill: number[], mana: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const skill: number[] = JSON.parse(inputValues[0]);
	const mana: number[] = JSON.parse(inputValues[1]);
	return minTime(skill, mana);
}
