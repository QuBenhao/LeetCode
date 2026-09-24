function braceExpansionII(expression: string): string[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const expression: string = JSON.parse(inputValues[0]);
	return braceExpansionII(expression);
}
