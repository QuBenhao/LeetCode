function numberOfSets(n: number, maxDistance: number, roads: number[][]): number {
    let res = 0;
    let opened = new Array(n).fill(0);

    for (let mask = 0; mask < (1 << n); mask++) {
        for (let i = 0; i < n; i++) {
            opened[i] = mask & (1 << i);
        }
        let d = new Array(n).fill(0).map(() => new Array(n).fill(1000000));

        for (let [i, j, r] of roads) {
            if (opened[i] > 0 && opened[j] > 0) {
                d[i][j] = d[j][i] = Math.min(d[i][j], r);
            }
        }

        // Floyd-Warshall algorithm
        for (let k = 0; k < n; k++) {
            if (opened[k] > 0) {
                for (let i = 0; i < n; i++) {
                    if (opened[i] > 0) {
                        for (let j = i + 1; j < n; j++) {
                            if (opened[j] > 0) {
                                d[i][j] = d[j][i] = Math.min(d[i][j], d[i][k] + d[k][j]);
                            }
                        }
                    }
                }
            }
        }

        // Validate
        let good = 1;
        for (let i = 0; i < n; i++) {
            if (opened[i] > 0) {
                for (let j = i + 1; j < n; j++) {
                    if (opened[j] > 0 && d[i][j] > maxDistance) {
                        good = 0;
                        break;
                    }
                }
                if (good == 0) {
                    break;
                }
            }
        }
        res += good;
    }
    return res;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const maxDistance: number = JSON.parse(inputValues[1]);
	const roads: number[][] = JSON.parse(inputValues[2]);
	return numberOfSets(n, maxDistance, roads);
}
