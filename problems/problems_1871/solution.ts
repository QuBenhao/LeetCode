function canReach(s: string, minJump: number, maxJump: number): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const minJump: number = JSON.parse(inputValues[1]);
	const maxJump: number = JSON.parse(inputValues[2]);
	return canReach(s, minJump, maxJump);
}
