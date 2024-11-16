function numFriendRequests(ages: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const ages: number[] = JSON.parse(inputValues[0]);
	return numFriendRequests(ages);
}
