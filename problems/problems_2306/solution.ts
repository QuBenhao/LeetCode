function distinctNames(ideas: string[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const ideas: string[] = JSON.parse(inputValues[0]);
	return distinctNames(ideas);
}
