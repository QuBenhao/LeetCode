function asteroidCollision(asteroids: number[]): number[] {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const asteroids: number[] = JSON.parse(inputValues[0]);
	return asteroidCollision(asteroids);
}
