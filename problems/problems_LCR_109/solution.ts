function openLock(deadends: string[], target: string): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const deadends: string[] = JSON.parse(inputValues[0]);
	const target: string = JSON.parse(inputValues[1]);
	return openLock(deadends, target);
}
