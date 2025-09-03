function findClosest(x: number, y: number, z: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const x: number = JSON.parse(inputValues[0]);
	const y: number = JSON.parse(inputValues[1]);
	const z: number = JSON.parse(inputValues[2]);
	return findClosest(x, y, z);
}
