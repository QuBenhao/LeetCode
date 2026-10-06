function distinctNames(ideas: string[]): number {
	const groups: Set<string>[] = Array.from({ length: 26 }, () => new Set());
	for (const s of ideas) {
		groups[s.charCodeAt(0) - 'a'.charCodeAt(0)].add(s.slice(1)); // Group by first letter
	}
	let ans: number = 0;
	for (let a: number = 1; a < 26; a++) { // Enumerate all pairs of groups
		for (let b: number = 0; b < a; b++) {
			let m: number = 0; // Size of the intersection
			for (const s of groups[a]) {
				if (groups[b].has(s)) {
					m++;
				}
			}
			ans += (groups[a].size - m) * (groups[b].size - m);
		}
	}
	return ans * 2; // Multiply by 2 at the end
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const ideas: string[] = JSON.parse(inputValues[0]);
	return distinctNames(ideas);
}
