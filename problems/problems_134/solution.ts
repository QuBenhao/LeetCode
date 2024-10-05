function canCompleteCircuit(gas: number[], cost: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const gas: number[] = JSON.parse(inputValues[0]);
	const cost: number[] = JSON.parse(inputValues[1]);
	return canCompleteCircuit(gas, cost);
}
