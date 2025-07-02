function kthCharacter(k: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const k: number = JSON.parse(inputValues[0]);
	return kthCharacter(k);
}
