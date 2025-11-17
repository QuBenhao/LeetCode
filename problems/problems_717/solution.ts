function isOneBitCharacter(bits: number[]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const bits: number[] = JSON.parse(inputValues[0]);
	return isOneBitCharacter(bits);
}
