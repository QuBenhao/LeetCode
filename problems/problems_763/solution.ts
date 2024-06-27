function partitionLabels(s: string): number[] {
	const last: number[] = new Array(26);
	for (let i: number = 0; i < s.length; i++) {
		last[s.charCodeAt(i) - 'a'.charCodeAt(0)] = i;
	}
	const partition: number[] = [];
	let start: number = 0, end: number = 0;
	for (let i: number = 0; i < s.length; i++) {
		end = Math.max(end, last[s.charCodeAt(i) - 'a'.charCodeAt(0)]);
		if (i === end) {
			partition.push(end - start + 1);
			start = end + 1;
		}
	}
	return partition;    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(splits[0]);
	return partitionLabels(s);
}
