function openLock(deadends: string[], target: string): number {
	const deadSet: Set<string> = new Set(deadends);
	const visited: Set<string> = new Set();
	const queue: string[] = ["0000"];
	let level: number = 0;
	while (queue.length > 0) {
		const size: number = queue.length;
		for (let i = 0; i < size; i++) {
			const current: string = queue.shift();
			if (deadSet.has(current)) {
				continue;
			}
			if (current === target) {
				return level;
			}
			for (let j = 0; j < 4; j++) {
				const up: string = current.substring(0, j) + (Number(current[j]) + 1) % 10 + current.substring(j + 1);
				if (!visited.has(up)) {
					queue.push(up);
					visited.add(up);
				}
				const down: string = current.substring(0, j) + (Number(current[j]) + 9) % 10 + current.substring(j + 1);
				if (!visited.has(down)) {
					queue.push(down);
					visited.add(down);
				}
			}
		}
		level++;
	}
	return -1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const deadends: string[] = JSON.parse(inputValues[0]);
	const target: string = JSON.parse(inputValues[1]);
	return openLock(deadends, target);
}
