function countTexts(pressedKeys: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const pressedKeys: string = JSON.parse(inputValues[0]);
	return countTexts(pressedKeys);
}
