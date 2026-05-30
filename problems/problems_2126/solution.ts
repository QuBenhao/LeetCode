function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const mass: number = JSON.parse(inputValues[0]);
	const asteroids: number[] = JSON.parse(inputValues[1]);
	return asteroidsDestroyed(mass, asteroids);
}
